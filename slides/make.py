"""
Pandoc Markdown to PDF Compiler with Watch Mode

This module provides a comprehensive solution for compiling Markdown files to PDF
using Pandoc with the Beamer template for creating presentation slides. It includes
advanced features such as:

- Automatic file watching for continuous compilation during editing
- Unicode character replacement for LaTeX compatibility
- MD5-based change detection to avoid unnecessary recompilation
- Configurable compilation parameters and error handling
- Support for bibliographies via pandoc-citeproc

The script is designed for academic and professional presentation workflows where
Markdown source files need to be continuously compiled to PDF as they are edited.

Usage
-----
Basic compilation:
    $ python make.py presentation.md

Watch mode (recompile on changes):
    $ python make.py presentation.md --watch

Custom sleep interval and verbose output:
    $ python make.py presentation.md -w -s 2.0 -v

Notes
-----
- Requires Pandoc and pandoc-citeproc to be installed
- Uses ../defaults.yaml for Pandoc configuration
- Automatically looks for references.bib in the working directory
- Beamer output format is specifically designed for presentations
"""

import os
import contextlib
import time
import hashlib
import argparse
import tempfile
from datetime import datetime

import sh

# Pre-configured Pandoc command template for Beamer presentations
# - t="beamer": Output format for LaTeX Beamer slides
# - d="../defaults.yaml": Custom defaults file for consistent styling
# - filter="pandoc-citeproc": Process citations and bibliography
# - verbose=True: Show detailed compilation output
PANDOC_CMD_TEMPLATE = sh.Command("pandoc").bake(
    t="beamer", d="../defaults.yaml", filter="pandoc-citeproc", verbose=True
)

# Unicode to LaTeX replacements for characters that don't render properly
# Add more mappings here as needed for special mathematical or typographic symbols
REPLACES = {
    "≠": r"$\neq$",  # Not equal sign
}


@contextlib.contextmanager
def chdir(newdir):
    """
    Context manager to temporarily change the working directory.

    Parameters
    ----------
    newdir : str
        Path to the new directory to change to.

    Yields
    ------
    None
        Control is yielded while in the new directory.

    Examples
    --------
    >>> with chdir('/tmp'):
    ...     print(os.getcwd())
    /tmp
    """
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)


def get_parser():
    """
    Create and configure the command line argument parser.

    Builds an ArgumentParser with all available command-line options for controlling
    the compilation process, including watch mode, sleep intervals, error handling,
    and verbosity settings.

    Returns
    -------
    argparse.ArgumentParser
        Configured argument parser with all required arguments and options:
        - archivo: Input Markdown file path (required positional argument)
        - --sleep/-s: Seconds to wait between file checks in watch mode (default: 1.5)
        - --watch/-w: Enable continuous compilation on file changes (default: False)
        - --ignore_error/-i: Continue on Pandoc errors (default: True)
        - --cd: Change to file directory before compilation (default: True)
        - --verbose/-v: Show detailed Pandoc output (default: False)

    Examples
    --------
    >>> parser = get_parser()
    >>> args = parser.parse_args(['file.md', '--watch'])
    >>> print(args.archivo, args.watch)
    file.md True

    Notes
    -----
    The --ignore_error flag uses store_false with default=True, meaning errors
    are ignored by default. To raise errors on Pandoc failures, do NOT use the flag.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "archivo",
        help="ruta del archivo a compilar",
        type=str,
    )
    parser.add_argument(
        "-s",
        "--sleep",
        help="segundos de espera",
        action="store",
        type=float,
        default=1.5,
    )
    parser.add_argument(
        "-w", "--watch", help="watch mode", action="store_true", default=False
    )
    parser.add_argument(
        "-i", "--ignore_error", action="store_false", default=True
    )
    parser.add_argument(
        "--cd",
        help="cambiar al directorio del archivo",
        action="store_true",
        default=True,
    )
    parser.add_argument("-v", "--verbose", action="store_true", default=False)
    return parser


def read_file(path):
    """
    Read the contents of a file.

    Parameters
    ----------
    path : str
        Path to the file to read.

    Returns
    -------
    str
        Contents of the file as a string.

    Raises
    ------
    FileNotFoundError
        If the specified file does not exist.
    IOError
        If there's an error reading the file.

    Examples
    --------
    >>> content = read_file('example.md')
    >>> print(len(content))
    1234
    """
    with open(path, "r") as f:
        return f.read()


def calculate_md5(src):
    """
    Calculate the MD5 hash of a string.

    Parameters
    ----------
    src : str
        The source string to hash.

    Returns
    -------
    str
        MD5 hash as a hexadecimal string.

    Examples
    --------
    >>> hash_value = calculate_md5("Hello World")
    >>> print(len(hash_value))
    32
    """
    return hashlib.md5(src.encode("utf-8")).hexdigest()


def process_unicode(src, fname, tempdir):
    """
    Process Unicode characters in source content and save to temporary file.

    This function replaces specific Unicode characters with their LaTeX equivalents
    to ensure proper rendering in the PDF output. The character mappings are defined
    in the REPLACES dictionary. The processed content is written to a temporary file
    that will be passed to Pandoc for compilation.

    Parameters
    ----------
    src : str
        Source content to process (the raw Markdown file contents).
    fname : str
        Original filename to use for the temporary file (preserves the file extension).
    tempdir : str
        Path to the temporary directory where the processed file will be saved.

    Returns
    -------
    str
        Absolute path to the processed temporary file.

    Examples
    --------
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     processed_path = process_unicode("a ≠ b", "test.md", tmpdir)
    ...     with open(processed_path) as f:
    ...         print(f.read())
    a $\neq$ b

    Notes
    -----
    The REPLACES dictionary at the module level defines which Unicode characters
    are replaced. Currently includes:
    - ≠ (not equal) -> $\neq$ (LaTeX not equal)

    Add more replacements to REPLACES as needed for additional Unicode characters.
    """
    output = os.path.join(tempdir, fname)
    for pattern, replace in REPLACES.items():
        src = src.replace(pattern, replace)

    with open(output, "w", encoding="utf-8") as f:
        f.write(src)

    return output


def run_pandoc(path, output_path, ignore_error, bibliography):
    """
    Execute Pandoc command to convert Markdown to PDF using Beamer template.

    This function runs Pandoc with pre-configured settings (Beamer template, citation
    processing, and custom defaults) to generate a PDF presentation from a Markdown file.
    It provides error handling options to allow compilation to continue even when Pandoc
    encounters issues.

    Parameters
    ----------
    path : str
        Path to the input Markdown file (typically a processed temporary file).
    output_path : str
        Path where the output PDF should be saved.
    ignore_error : bool
        Whether to ignore Pandoc errors and continue execution. If True, errors are
        printed but don't stop the program. If False, errors are raised.
    bibliography : str
        Path to the bibliography file (.bib) for citation processing. Currently passed
        as a parameter but not used in the function implementation.

    Returns
    -------
    sh.RunningCommand or None
        Pandoc command result if successful, None if error was ignored.

    Raises
    ------
    sh.ErrorReturnCode
        If Pandoc execution fails and ignore_error is False.

    Examples
    --------
    >>> run_pandoc("input.md", "output.pdf", ignore_error=True, bibliography="refs.bib")

    Notes
    -----
    The function uses PANDOC_CMD_TEMPLATE which is pre-configured with:
    - Beamer output format for presentations
    - Citation processing via pandoc-citeproc
    - Custom defaults from ../defaults.yaml
    - Verbose output enabled
    """
    pandoc = PANDOC_CMD_TEMPLATE.bake(path, output=output_path)
    try:
        output = pandoc()
        return output
    except sh.ErrorReturnCode as err:
        if ignore_error:
            print("=======================")
            print(">>> IGNORANDO ERROR <<<")
            print("=======================")
            print(err)
        else:
            raise err


def main():
    """
    Main function that orchestrates the Markdown to PDF compilation process.

    This function handles command line argument parsing, file monitoring,
    and coordinates the compilation process. It supports both single compilation
    and watch mode for continuous compilation on file changes.

    Workflow
    --------
    1. Parse command line arguments to get file path and options
    2. Set up working directory (either current dir or file's directory)
    3. Create temporary directory for processed files
    4. Read source file and calculate MD5 hash for change detection
    5. Process Unicode characters to LaTeX equivalents
    6. Compile to PDF using Pandoc with Beamer template
    7. If watch mode enabled, continuously monitor file for changes:
       - Check file every N seconds (configurable via --sleep)
       - Recalculate MD5 hash on each check
       - Recompile only if content has changed

    Environment
    -----------
    The function operates within two context managers:
    - chdir: Changes to the appropriate working directory
    - TemporaryDirectory: Creates a temp directory for processed files

    File Paths
    ----------
    - Input: Original .md file specified by user
    - Processed: Temporary file with Unicode replacements
    - Output: PDF file with same name as input (replaces .md with .pdf)
    - Bibliography: references.bib in working directory (if exists)

    Examples
    --------
    Single compilation:
        $ python make.py presentation.md

    Watch mode with custom interval:
        $ python make.py presentation.md --watch --sleep 2.0

    Verbose output with error handling:
        $ python make.py presentation.md -w -v -i

    Notes
    -----
    - The MD5 hash is used to detect file changes efficiently without comparing
      entire file contents
    - Unicode processing happens before each compilation to ensure LaTeX compatibility
    - The temporary directory is automatically cleaned up when the program exits
    - In watch mode, the loop continues indefinitely until interrupted (Ctrl+C)
    """

    # Parse command line arguments
    parser = get_parser()

    args = parser.parse_args()
    sleep = args.sleep
    original_path = args.archivo
    watch = args.watch
    ignore_error = args.ignore_error
    cd = args.cd
    verbose = args.verbose

    # Determine working directory: either current directory or the file's directory
    wd = sh.pwd().strip()
    filepath = original_path
    if cd:
        # Change to the file's directory for easier relative path handling
        wd = os.path.dirname(filepath)
        filepath = os.path.basename(filepath)

    # Set up output paths
    output_path = filepath.replace(".md", ".pdf")
    bibliography_path = os.path.join(wd, "references.bib")

    # Work within the appropriate directory and a temporary directory for processing
    with chdir(wd), tempfile.TemporaryDirectory() as tempdir:

        if watch:
            msg = f">>>>>> Watching every {sleep} seconds for changes in {original_path!r} <<<<<<"
            print("=" * len(msg))
            print(msg)
            print("=" * len(msg))

        # Initial compilation: read file and calculate hash for change detection
        src = read_file(filepath)
        md5 = calculate_md5(src)
        processed_path = process_unicode(src, filepath, tempdir)

        # Show compilation details
        print("Proccesed file:", processed_path)
        print("Command:", PANDOC_CMD_TEMPLATE)
        print("")
        now = datetime.now().strftime("%H:%M:%S")
        print(
            f"[{now}] Compiling",
            original_path,
            "->",
            os.path.join(wd, output_path),
        )

        # Run initial compilation
        output = run_pandoc(
            processed_path,
            output_path,
            ignore_error,
            bibliography=bibliography_path,
        )
        if verbose:
            print(output)

        # Watch mode: continuously monitor file for changes
        while watch:
            time.sleep(sleep)

            # Read file and check if it has changed
            src = read_file(filepath)
            new_md5 = calculate_md5(src)

            if md5 != new_md5:
                # File has changed, recompile
                now = datetime.now().strftime("%H:%M:%S")
                print(
                    f"[{now}] Compiling",
                    original_path,
                    "->",
                    os.path.join(wd, output_path),
                )
                processed_path = process_unicode(src, filepath, tempdir)
                output = run_pandoc(
                    processed_path,
                    output_path,
                    ignore_error,
                    bibliography=bibliography_path,
                )
                if verbose:
                    print(output)
                # Update hash for next comparison
                md5 = new_md5


if __name__ == "__main__":
    main()

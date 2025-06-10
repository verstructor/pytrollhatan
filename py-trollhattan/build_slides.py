"""
Script to convert all Jupyter notebooks in the 'notebooks/' directory
to HTML slides using nbconvert. Slides are saved in both each notebook's
'slides/' subfolder and the top-level 'slides/' directory.
"""

from pathlib import Path
import shutil
import subprocess

NOTEBOOKS_DIR = Path("notebooks")
TOPLEVEL_SLIDES_DIR = Path("slides")

def ensure_dir(path):
    """Create directory if it does not exist."""
    Path(path).mkdir(parents=True, exist_ok=True)

def convert_notebook_to_slides(notebook_path, output_dir, output_filename):
    """
    Convert a notebook to HTML slides using nbconvert.
    """
    cmd = [
        "jupyter", "nbconvert",
        "--to", "slides",
        "--output", output_filename,  # Only filename, no path or extension
        "--output-dir", str(output_dir),
        str(notebook_path)
    ]
    subprocess.run(cmd, check=True)

def main():
    # Find all .ipynb files in subfolders of NOTEBOOKS_DIR
    notebook_files = NOTEBOOKS_DIR.glob("*/" + "*.ipynb")

    ensure_dir(TOPLEVEL_SLIDES_DIR)

    for nb_path in notebook_files:
        nb_dir = nb_path.parent
        nb_name = nb_path.stem
        slides_subdir = nb_dir / "slides"
        ensure_dir(slides_subdir)

        # Output filename (without extension)
        output_filename = nb_name

        # Convert notebook to slides in the notebook's slides/ subfolder
        convert_notebook_to_slides(nb_path, slides_subdir, output_filename)

        # Source and destination for copying to top-level slides/
        html_slide_file = slides_subdir / f"{output_filename}.slides.html"
        dest_slide_file = TOPLEVEL_SLIDES_DIR / f"{nb_name}.html"
        shutil.copy2(html_slide_file, dest_slide_file)

        print(f"Converted {nb_path} -> {dest_slide_file}")

if __name__ == "__main__":
    main()

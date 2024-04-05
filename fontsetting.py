# The following function modifies the behavior of "plt" to ensure that the text (labels, titles, etc.) on the figures is typeset using the Computer Modern font.
# If you don't have "TexLive" installed, you can get it from [here](https://www.tug.org/mactex/) (macOS) or [here](https://tug.org/texlive/acquire-netinstall.html) (Windows). 
# Note, macOS users will need to manually provide the path to "texlive" in the following cell.

def font_cmu(plt):
    import os
    os.environ["PATH"] += os.pathsep + "/usr/local/texlive/2022/bin/universal-darwin"  # This line is needed for macOS; update path on the location f TexLive on your system
    plt.rcParams["text.latex.preamble"] = r"\usepackage{bm} \usepackage{amsmath}"

    params = {"text.usetex": True,
            # "font.size": 12,
            "font.family": "cm",
            "legend.fontsize": "large",
            "figure.figsize": (15, 5),
            "axes.titlesize": "xx-large",
            "axes.labelsize": "x-large",
            "xtick.labelsize": "large",
            "ytick.labelsize": "large"}
    plt.rcParams.update(params)
    plt.rc("text.latex", preamble=r"\usepackage{underscore}")  # This line is to ensure that LaTeX reads "_" as "\_" in filenames
    return plt
In order to setup everything, just copy this repo.
- Search and replace all names

Followed this guide: https://blog.esciencecenter.nl/versioned-documentation-using-only-github-actions-and-github-pages-1825296e31aa
And used the repo as basis.

# GH-Pages

Add the following files manualy to gh-pages branch:
- `.nojekyll`
    - An empty file
```
Jekyll Configuration: GitHub Pages uses Jekyll to build static websites. Jekyll has certain default behaviors, such as ignoring files or directories that start with an underscore (_). Since your directory is named _static, it might be ignored by Jekyll. You can override this behavior by adding a .nojekyll file to the root of your gh-pages branch, which you already have according to the directory listing you provided. Make sure that the .nojekyll file is present in the root of the gh-pages branch on GitHub as well.
```
- `index.html`
    - This will redirect to the latest version
```
<html>
<head>
<meta http-equiv="refresh" content="0; url=latest/" />
</head>
</html>
```

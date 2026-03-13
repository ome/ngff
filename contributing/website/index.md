# Changes to this website

The repository for this website is [ome/ngff](https://github.com/ome/ngff).
Contributions to these pages are welcome as issues or PRs.

To do so, create a fork of the ``ome/ngff`` repository, make your changes,
and submit a pull request (PR) against the `main` branch.

## Configuration
Edit [conf.py](https://github.com/ome/ngff/blob/main/conf.py) with options from the [PyData Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/). The [PyData Sphinx Theme](https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html) user guide may also have more up to date instructions for configuration properties.

## Building the pages locally

Before submitting changes to the ngff website,
please build the pages locally and make sure that everything renders correctly.

To do so, first install a few necessary (Python) dependencies:

```bash
cd path/to/ngff/repo
pip install -r requirements.txt
pip install specifications/dev
```

Then, you can build the pages locally with:

```bash
make html
```

or 

```bash
python conf.py
```

You can then find the rendered pages under `_build/html/index.html`.

## Previews
Each PR receives a unique preview URL of the format `https://ngff--<PR#>.org.readthedocs.build/` where `<PR#>` is the PR number. This link is also posted to each PR by the Github actions bot in an "Automated Review URLs" comment as the "Readthedocs" link.

Please check that your changes render correctly at this URL. New commits will automatically be live at the PR url after a few minutes.
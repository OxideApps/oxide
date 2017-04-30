import setuptools

setuptools.setup(
    name="odoo10-oxide",
    description="Meta package for Odoo 10 Oxide addons",
    version="10.0.0.1.0",
    setup_requires=['setuptools-odoo'],
    odoo_addons=True,
)

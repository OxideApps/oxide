# Oxide
The community powered Odoo distribution.

Oxide is a ready to use Odoo distribution, 
based on Odoo Community Edition (or OCB),
packaged with selected community addons
to provide the best user experience Odoo CE can give.

## Getting started

Oxide was designed to work with the standard Python tools
``virtualenv`` and ``pip``.


	 $ # Prepare a Pyhton environment to work in
	 $ virtualenv MyProject
	 $ source MyProject/bin/activate
	 $ # Install Odoo
     $ git clone https://github.com/odoo/odoo.git --depth=1
     $ pip install -e ./odoo
     $ # Install Oxide
     $ pip install -e https://github.com/OxideApps/oxide.git@10.0#egg=oxide
     $ odoo start -i base_oxide

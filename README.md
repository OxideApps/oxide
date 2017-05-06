# Oxide

The community powered Odoo distribution.

Oxide is a ready to use Odoo distribution, 
based on Odoo Community Edition (Odoo CE),
packaged tigether with selected community addons
to provide the best user experience Odoo CE can give.


## Getting started

Oxide was designed to work with the standard Python tools
`virtualenv` and `pip`.

But first we need to have Odoo and dependencies installed in our system.
The following will get Odoo ready for us:

    $ git clone https://github.com/odoo/odoo.git --depth=1
    $ ./odoo/setup/setup_dev.py setup_deps 
    $ ./odoo/setup/setup_dev.py setup_pg 

Now we can install Oxide. 
We will  be using a Pyhton virtual environment for that:

    $ virtualenv MyProject
    $ source MyProject/bin/activate
    $ pip install -e ./odoo
    $ pip install -e https://github.com/OxideApps/oxide.git@10.0#egg=oxide
    $ odoo start -i base_oxide
 

## The Oxide manifest

The goal for Oxide is to provide, out of the box, 
the best possible user experience for Odoo CE.

Oxide improvements over Odoo CE are expected 
to be mostly generic usability features, 
for both regular and power users. 

For example, improved app and menu navigation, 
better design on mobile devices, 
or advanced data search features.

Business logic features may also enter the roadmap, 
but from the perspective of providing a app capabilities,
rather than specializing in some specific business area.

Oxide also intends to make a statement about how Odoo apps are
distributed and administered.
Python tools like `virtualenv`, `pip` and PyPI should be fully supported, 
and considered the default approach for Oxide and addon distribution,
both on the CLI and on the GUI.
They should "just work".

Another long term goal for Oxide is to aid people in 
upgrading and migration their instances.
These are complex issues, but we aim to work on steps
to make it easier, and as close to "just works" as possible.


## Aren't some of these features already available?

Yes. The Oxide approach is to select and package together the best 
the community can provide.
The focus should be on reuse and collaboration.
Rather the developing features itself, Oxide collaborators should instead
work with upstream projects to adjust and create the features needed by
Oxide.
So, another goal is to be a motivator and driving force 
to improve and build community features.


## Will Oxide be compatible with existing addon modules

Absolutely. In the end, Oxide is just a flavour of Odoo CE and is expected to be
fully compatible with any addon modules that work on Odoo CE.


## If Odoo CE is not good enough, why not doing a fork instead?

For three reasons.

First, we don't need a fork to achieve the project goals.
What takes Odoo apart from other frameworks is the ability to be extended.
Using addon extensions alone, we can do pretty much what we need.
In the corner cases where that is not practical, we can work upstream with
Odoo SA to add the needed extension hooks. The worst case scenario is to have to maintain 
a few key patches to Odoo CE, and in this case the Odoo Community Backports (OCB)
project would surely help.

Second, a long term fork makes the community weaker.
Is is the nature of a fork that, sooner than later, 
there will be incompatibilities with Odoo CE.
And then we will have addons and apps that work on one version but not on the other.
And as developers choose sides, the community is split in two, 
they both grow slower and duplicate efforts.

Third, a fork would surely waste the effort Odoo SA puts into the Community Edition.
While it would still be possible to incorporate into the fork
changes added to Odoo CE, it will require significant effort and won't be practical
in the long run. The consequence of this is that it won't be able to take advantage
of the work of dozens of full-time engineers from Odoo SA.

# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import config as cfg
from core.ui import WindowWrapper


def main():
    print("Note: closing this window will close Bob's Brewery.")

    root = WindowWrapper.load_window_from_file(rf"{cfg.source_root}\core\ui\ui_elements\windows\main_window.json")
    root.window.mainloop()


main()

'''
I ought to put all the current data access things in the contact management module since that is the only thing using
any of it. Really the core - if it uses a database - and each module that uses a database should each have their own
self-contained databases, DALs, etc. Nothing should be tightly coupled, as modularity is the keyword for this tool.

That will probably be a branch in the near future after the add contacts one is done.

I should also get module management working so that modules are not manually imported anywhere but are managed by a
ModuleManager class or similar which leverages the module registry and an enforces core/modules/module_name route to
the root of each module. As I started to define above, every module should consider itself logically bound by its root
directory except in the case of a module - if any exist - whose purpose is to change the behavior of other modules or of
the core, but I am skeptical whether anything like that will exist. Themes should not be so bound, but a theme is not a
module.

Setting that up, of course, will probably be its own branch.

Another branch will probably be to implement the option for framing rather than packing. I will keep packing as an
option, especially since it is useful for prototyping, but framing gives a lot more flexibility in UI design. This, of
course, needs to be able to be json-driven, as json (and possibly yaml if it can be pulled in as dictionaries as json
can so that the already existing code can handle it properly as long as it is loaded correctly) is central to the goal
of allowing relatively non-technical people to build graphical tools without too steep a learning curve. It also makes
it easier for tech people to manage things in some ways. Also, if I do build a wysiwyg editor, having it work by
creating json/yaml files to be loaded by the program will make it pretty straightforward for people to fine-tune things
as needed.

Aaaaaaand another branch... Gotta firm up security. Query execution, for example, works but is not secure at the moment.
Need to look into other areas for improvement regarding security too. The sql part of this will also probably include
putting commonly used queries (whether in core or a module) in a queries.py file in the appropriate core/module location
to be stored there as constants

Should probably get a Notion going for this whole thing.
'''
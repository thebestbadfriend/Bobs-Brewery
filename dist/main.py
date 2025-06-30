# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import config as cfg
from core.ui import WindowWrapper


def main():
    print("Note: closing this window will close Bob's Brewery.")

    root = WindowWrapper.load_window_from_file(rf"{cfg.source_root}\core\ui\ui_elements\windows\main_window.json")
    root.window.mainloop()


main()

'''
check for updates (auto on start and also a check for updates button). Auto check on start should be toggleable via
a checkbox in settings (so also need a settings menu)

main window should not have its json quite so hard coded. The core of the UI can be, but since modules may arbitrarily
exist and be loaded, some kind of loop will need to handle the folding of module UI into the display and the application
of themes

I ought to put all the current data access things in the contact management module since that is the only thing using
any of it. Really the core - if it uses a database - and each module that uses a database should each have their own
self-contained databases, DALs, etc. Nothing should be tightly coupled, as modularity is the keyword for this tool.

Basically, brewerydbaccessor should probably be configured to use a "bb_core" database by default but to accept other
DBs so that bb_contacts, for example, can be used, but the logic for core should be in core, for contacts should be
in contacts, etc.

That will probably be a branch in the near future after the add contacts one is done.

also, per-module configs. Nothing special needs to be done - I think - to make each module able to have its own config
file, but the current config.py should go into the core folder, as it should be the core config. contact management
should have its own config.py file. And so on. If a config file is to exist at the root of the project (in the same dir
as main.py), then it should be clearly named something like global_config.py to indicate that it is for settings that
are not bound by the scope of core or of any one module. This separation of configs will allow for things like
Obsidian's per-plugin settings menus where you can go into each plugin and configure that plugin's settings pretty
organically.

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

Another, some improved utility and separation of concerns for db stuff. the db accessor should probably not only accept
queries but also provide flexible functions for common practices such as a get_column_by_column function something like
    def get_column_by_column(db, table, column_to_get, column_to_search_by, db_user='', db_pass='')

Should probably get a Notion going for this whole thing.

meta folder structure for yaml/json files representing data types, classes, etc and all the relevant properties,
functions, events/bindings, etc for each. (see chatgpt conversation)

code completion

inspector pane

"script runner" module. Basically a multiline text input that allows a script to by typed or pasted in, a browse button
to allow selecting an existing script, a run now, scheduled run, and run at interval option, and a dropdown to select a
supported language so that, for example, if you want to ping google every 15 seconds and log whether it worked, you can
just do the ping and log commands without having to set up the schedule. Maybe also an output dropdown to allow
outputting to a file, to a sort of inline console, discarding output, etc. And maybe an "alert if error" checkbox or
similar.

---

If I do go the 'something like visual studio for python' or 'something like godot but for general python application
dev, one clear benefit of that, which I do not want to forget, is that the ability to drag and drop widgets and to click
on them to pull up something like the inspector window in Godot which shows properties, signals/events/bindings, etc
means that people do not have to know what things are called, what properties/events/etc they come with, etc. The editor
can tell them all of that and even - where it is useful - show things as more user-friendly names
(e.g. on_node_expanded rather than <<TreeviewOpen>>) and provide on-hover descriptions of what things do. This might
actually be one of the most important elements of all for the goal of making it hyper-accessible to relatively
non-technical users.
'''
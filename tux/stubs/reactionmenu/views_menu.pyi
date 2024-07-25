"""
This type stub file was generated by pyright.
"""

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Literal, NamedTuple, overload

import discord
from discord.ext.commands import Context

from . import ViewButton
from .abc import MenuType, Page, _BaseMenu
from .decorators import ensure_not_primed
from .errors import *

"""
MIT License

Copyright (c) 2021-present @defxult

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE.
"""
if TYPE_CHECKING: ...
_SelectOptionRelayPayload = ...

class ViewSelect(discord.ui.Select):
    """A class to assist in the process of categorizing information on a :class:`ViewMenu`

    Parameters
    ----------
    title: Union[:class:`str`, `None`]
        The category name. If `None`, the category name defaults to "Select a category"

    options: Dict[:class:`discord.SelectOption`, List[:class:`Page`]]
        A key/value pair associating the category options with pages to navigate

    disabled: :class:`bool`
        If the select should start enabled or disabled

        .. added:: v3.1.0
    """
    def __init__(
        self, *, title: str | None, options: dict[discord.SelectOption, list[Page]], disabled: bool = ...
    ) -> None: ...
    def __repr__(self) -> str: ...
    @property
    def menu(self) -> ViewMenu | None:
        """
        Returns
        -------
        Optional[:class:`ViewMenu`]: The menu this select is attached to. Can be `None` if not attached to any menu
        """

    async def callback(self, interaction: discord.Interaction) -> None:
        """*INTERNAL USE ONLY* - The callback function from the select interaction. This should not be manually called"""

    class GoTo(discord.ui.Select):
        """Represents a UI based version of a :class:`ViewButton` with the ID `ViewButton.ID_GO_TO_PAGE`

        Parameters
        ----------
        title: Union[:class:`str`, `None`]
            The selects name. If `None`, the name defaults to "Navigate to page..."

        page_numbers: This parameter accepts 3 different types and are explained below
        - List[:class:`int`]
            - If set to a list of integers, those specified values are the only options that are available when the select is clicked

        - Dict[:class:`int`, Union[:class:`str`, :class:`discord.Emoji`, :class:`discord.PartialEmoji`]]
            - You can use this type if you'd like to utilize emojis in your select options

        - `ellipsis`
            - Set an ellipsis to have the library automatically assign all page numbers to the amount of pages that you've added to the menu.

        NOTE: Setting the `page_numbers` parameter to an ellipsis (...) only works as intended if you've added the go to select AFTER you've added pages to the menu

            .. added:: v3.1.0
        """
        def __init__(
            self,
            *,
            title: str | None,
            page_numbers: list[int] | dict[int, str | discord.Emoji | discord.PartialEmoji] | ellipsis,
        ) -> None: ...
        @property
        def menu(self) -> ViewMenu | None:
            """
            Returns
            -------
            Optional[:class:`ViewMenu`]: The menu this select is attached to. Can be `None` if not attached to any menu
            """

class ViewMenu(_BaseMenu):
    """A class to create a discord pagination menu using :class:`discord.ui.View`

    Parameters
    ----------
    method: Union[:class:`discord.ext.commands.Context`, :class:`discord.Interaction`]
        The Context object. You can get this using a command or if you're in a `discord.on_message` event. Also accepts interactions, typically received when using slash commands

    menu_type: :class:`MenuType`
        The configuration of the menu. Class variables :attr:`ViewMenu.TypeEmbed`, :attr:`ViewMenu.TypeEmbedDynamic`, or :attr:`ViewMenu.TypeText`

    Kwargs
    ------
    all_can_click: :class:`bool`
        Sets if everyone is allowed to control when pages are 'turned' when buttons are pressed (defaults to `False`)

    allowed_mentions: :class:`discord.AllowedMentions`
        Controls the mentions being processed in the menu message (defaults to :class:`discord.AllowedMentions(everyone=False, users=True, roles=False, replied_user=True)`).
        Not valid for `ViewMenu` with a `menu_type` of `TypeText`

    custom_embed: :class:`discord.Embed`
        Embed object to use when adding data with :meth:`ViewMenu.add_row()`. Used for styling purposes only (:attr:`ViewMenu.TypeEmbedDynamic` only/defaults to :class:`None`)

    delete_interactions: :class:`bool`
        Delete the prompt message by the bot and response message by the user when asked what page they would like to go to when using :attr:`ViewButton.ID_GO_TO_PAGE` (defaults to `True`)

    delete_on_timeout: :class:`bool`
        Delete the menu when it times out (defaults to `False`) If `True`, :attr:`disable_items_on_timeout` and :attr:`remove_items_on_timeout` will not execute regardless of if they are `True`. This takes priority over those actions

    disable_items_on_timeout: :class:`bool`
        Disable the buttons on the menu when the menu times out (defaults to `True`) If :attr:`delete_on_timeout` is `True`, this will be overridden

    name: :class:`str`
        A name you can set for the menu (defaults to :class:`None`)

    only_roles: List[:class:`discord.Role`]
        If set, only members with any of the given roles are allowed to control the menu. The menu owner can always control the menu (defaults to :class:`None`)

    remove_items_on_timeout: :class:`bool`
        Remove the buttons on the menu when the menu times out (defaults to `False`) If :attr:`disable_items_on_timeout` is `True`, this will be overridden

    rows_requested: :class:`int`
        The amount of information per :meth:`ViewMenu.add_row()` you would like applied to each embed page (:attr:`ViewMenu.TypeEmbedDynamic` only/defaults to :class:`None`)

    show_page_director: :class:`bool`
        Shown at the bottom of each embed page. "Page 1/20" (defaults to `True`)

    style: :class:`str`
        A custom page director style you can select. "$" represents the current page, "&" represents the total amount of pages (defaults to "Page $/&") Example: `ViewMenu(ctx, ..., style='On $ out of &')`

    timeout: Union[:class:`int`, :class:`float`, :class:`None`]
        The timer for when the menu times out. Can be :class:`None` for no timeout (defaults to `60.0`)

    wrap_in_codeblock: :class:`str`
        The discord codeblock language identifier to wrap your data in (:attr:`ViewMenu.TypeEmbedDynamic` only/defaults to :class:`None`). Example: `ViewMenu(ctx, ..., wrap_in_codeblock='py')`
    """

    _active_sessions: list[ViewMenu] = ...
    def __init__(self, method: Context | discord.Interaction, /, *, menu_type: MenuType, **kwargs) -> None: ...
    def __repr__(self):  # -> str:
        ...
    @property
    def selects(self) -> list[ViewSelect]:
        """
        Returns
        -------
        List[:class:`ViewSelect`]: All selects that have been added to the menu

            .. added:: v3.1.0
        """

    @property
    def go_to_selects(self) -> list[ViewSelect.GoTo]:
        """
        Returns
        -------
        List[:class:`ViewSelect.GoTo`]: All go to selects that have been added to the menu

            .. added:: v3.1.0
        """

    @property
    def timeout(self):  # -> int | float | None:
        ...
    @timeout.setter
    def timeout(self, value) -> int | float | None:
        """A property getter/setter for kwarg `timeout`"""

    @property
    def buttons(self) -> list[ViewButton]:
        """
        Returns
        -------
        List[:class:`ViewButton`]: All buttons that have been added to the menu
        """

    @property
    def buttons_most_clicked(self) -> list[ViewButton]:
        """
        Returns
        -------
        List[:class:`ViewButton`]: The list of buttons on the menu ordered from highest (button with the most clicks) to lowest (button with the least clicks). Can be an empty list if there are no buttons registered to the menu
        """

    @classmethod
    async def quick_start(
        cls,
        method: Context | discord.Interaction,
        /,
        pages: Sequence[discord.Embed | str],
        buttons: Sequence[ViewButton] | None = ...,
    ) -> ViewMenu:
        """|coro class method|

        Start a menu with default settings either with a `menu_type` of `ViewMenu.TypeEmbed` (all values in `pages` are of type `discord.Embed`) or `ViewMenu.TypeText` (all values in `pages` are of type `str`)

        Parameters
        ----------
        method: Union[:class:`discord.ext.commands.Context`, :class:`discord.Interaction`]
            The Context object. You can get this using a command or if you're in a `discord.on_message` event. Also accepts interactions, typically received when using slash commands

        pages: Sequence[Union[:class:`discord.Embed`, :class:`str`]]
            The pages to add

        buttons: Optional[Sequence[:class:`ViewButton`]]
            The buttons to add. If left as `DEFAULT_BUTTONS`, that is equivalent to `ViewButton.all()`

        Returns
        -------
        :class:`ViewMenu`: The menu that was started

        Raises
        ------
        - `MenuAlreadyRunning`: Attempted to call method after the menu has already started
        - `NoPages`: The menu was started when no pages have been added
        - `NoButtons`: Attempted to start the menu when no Buttons have been registered
        - `IncorrectType`: All items in :param:`pages` were not of type :class:`discord.Embed` or :class:`str`

            .. added v3.1.0
        """

    def set_select_option_relay(self, func: Callable[[NamedTuple], None], *, only: Sequence[str] | None = ...) -> None:
        """Set a function to be called with a given set of information when a select option is pressed on the menu. The information passed is `SelectOptionRelayPayload`, a named tuple.
        The named tuple contains the following attributes:

        - `member`: The :class:`discord.Member` object of the person who pressed the option. Could be :class:`discord.User` if the menu was started in a DM
        - `option`: The :class:`discord.SelectOption` that was pressed
        - `menu`: An instance of :class:`ViewMenu` that the select option is operating under

        Parameters
        ----------
        func: Callable[[:class:`NamedTuple`], :class:`None`]
            The function should only contain a single positional argument. Command functions (`@bot.command()`) not supported

        only: Optional[Sequence[:class:`str`]]
            A sequence of :class:`discord.SelectOption` labels associated with the current menu instance. If this is :class:`None`, all select options on the menu will be relayed.
            If set, only presses from the options matching the given labels specified will be relayed

        Raises
        ------
        - `IncorrectType`: The :param:`func` argument provided was not callable

            .. added:: v3.1.0
        """

    def remove_select_option_relay(self) -> None:
        """Remove the select option relay that's been set

        .. added:: v3.1.0
        """

    @ensure_not_primed
    def add_select(self, select: ViewSelect) -> None:
        """Add a select category to the menu

        Parameters
        ----------
        select: :class:`ViewSelect`
            The category listing to add

        Raises
        ------
        - `MenuAlreadyRunning`: Attempted to call method after the menu has already started
        - `ViewMenuException`:  The `menu_type` was not of :attr:`TypeEmbed`. The "embed" parameter in a :class:`Page` was not set. Or both :class:`ViewSelect` and a :class:`ViewSelect.GoTo` were being used

            .. added:: v3.1.0
        """

    def remove_select(self, select: ViewSelect) -> None:
        """Remove a select from the menu

        Parameters
        ----------
        select: :class:`ViewSelect`
            The select to remove

        Raises
        ------
        - `SelectNotFound`: The provided select was not found in the list of selects on the menu

            .. added:: v3.1.0
        """

    def remove_all_selects(self) -> None:
        """Remove all selects from the menu

        .. added:: v3.1.0
        """

    def disable_select(self, select: ViewSelect) -> None:
        """Disable a select on the menu

        Parameters
        ----------
        select: :class:`ViewSelect`
            The select to disable

        Raises
        ------
        - `SelectNotFound`: The provided select was not found in the list of selects on the menu

            .. added:: v3.1.0
        """

    def disable_all_selects(self) -> None:
        """Disable all selects on the menu

        .. added:: v3.1.0
        """

    def enable_select(self, select: ViewSelect) -> None:
        """Enable the specified select

        Parameters
        ----------
        select: :class:`ViewSelect`
            The select to enable

        Raises
        ------
        - `SelectNotFound`: The provided select was not found in the list of selects on the menu

            .. added:: v3.1.0
        """

    def enable_all_selects(self) -> None:
        """Enable all selects on the menu

        .. added:: v3.1.0
        """

    @overload
    def get_select(self, title: str) -> list[ViewSelect]: ...
    @overload
    def get_select(self, title: None) -> list[ViewSelect]: ...
    def get_select(self, title: str | None) -> list[ViewSelect]:
        """Get a select by it's title (category name) that has been registered to the menu

        Parameters
        ----------
        title: Union[:class:`str`, `None`]
            Title of the category

        Returns
        -------
        List[:class:`ViewSelect`]: All selects matching the given title
        """

    @ensure_not_primed
    def add_go_to_select(self, goto: ViewSelect.GoTo) -> None:
        """Add a select where the user can choose which page they'd like to navigate to.

        Parameters
        ----------
        goto: :class:`ViewSelect.GoTo`
            The navigation listing

        Raises
        ------
        - `MenuAlreadyRunning`: Attempted to call method after the menu has already started
        - `ViewMenuException`:  A :class:`ViewSelect` was already added to the menu. A :class:`ViewSelect` and a :class:`ViewSelect.GoTo` cannot both be used on a single menu

            .. added:: v3.1.0
        """

    def enable_go_to_select(self, goto: ViewSelect.GoTo) -> None:
        """Enable the specified go to select

        Parameters
        ----------
        goto: :class:`ViewSelect.GoTo`
            The go to select to enable

            .. added:: v3.1.0
        """

    def enable_all_go_to_selects(self) -> None:
        """Enable all go to selects

        .. added:: v3.1.0
        """

    def disable_go_to_select(self, goto: ViewSelect.GoTo) -> None:
        """Disable the specified go to select

        Parameters
        ----------
        goto: :class:`ViewSelect.GoTo`
            The go to select to disable

            .. added:: v3.1.0
        """

    def disable_all_go_to_selects(self) -> None:
        """Disable all go to selects

        .. added:: v3.1.0
        """

    def remove_go_to_select(self, goto: ViewSelect.GoTo) -> None:
        """Remove a go to select from the menu

        Parameters
        ----------
        goto: :class:`ViewSelect.GoTo`
            The go to select to remove

        Raises
        ------
        - `SelectNotFound`: The provided go to select was not found in the list of selects on the menu

            .. added:: v3.1.0
        """

    def remove_all_go_to_selects(self) -> None:
        """Remove all go to selects from the menu

        .. added:: v3.1.0
        """

    async def update(
        self, *, new_pages: list[discord.Embed | str] | None, new_buttons: list[ViewButton] | None
    ) -> None:
        """|coro|

        When the menu is running, update the pages or buttons. It should be noted that `ViewSelect`s are not supported here, and they will automatically be removed
        once the menu is updated. This method only supports pages and buttons.

        Parameters
        ----------
        new_pages: List[Union[:class:`discord.Embed`, :class:`str`]]
            Pages to *replace* the current pages with. If the menus current `menu_type` is :attr:`ViewMenu.TypeEmbed`, only :class:`discord.Embed` can be used. If :attr:`ViewMenu.TypeText`, only :class:`str` can be used. If you
            don't want to replace any pages, set this to :class:`None`

        new_buttons: List[:class:`ViewButton`]
            Buttons to *replace* the current buttons with. Can be an empty list if you want the updated menu to have no buttons. Can also be set to :class:`None` if you don't want to replace any buttons

        Raises
        ------
        - `ViewMenuException`: The :class:`ViewButton` custom_id was not recognized or a :class:`ViewButton` with that ID has already been added
        - `TooManyButtons`: There are already 25 buttons on the menu
        - `IncorrectType`: The values in :param:`new_pages` did not match the :class:`ViewMenu`'s `menu_type`. An attempt to use this method when the `menu_type` is :attr:`ViewMenu.TypeEmbedDynamic` which is not allowed. Or
        all :param:`new_buttons` values were not of type :class:`ViewButton`
        """

    def randomize_button_styles(self) -> None:
        """Set all buttons currently registered to the menu to a random :class:`discord.ButtonStyle` excluding link buttons"""

    def set_button_styles(self, style: discord.ButtonStyle) -> None:
        """Set all buttons currently registered to the menu to the specified :class:`discord.ButtonStyle` excluding link buttons

        Parameters
        ----------
        style: :class:`discord.ButtonStyle`
            The button style to set
        """

    async def refresh_menu_items(self) -> None:
        """|coro|

        When the menu is running, update the message to reflect the buttons/selects that were removed, enabled, or disabled
        """

    def remove_button(self, button: ViewButton) -> None:
        """Remove a button from the menu

        Parameters
        ----------
        button: :class:`ViewButton`
            The button to remove

        Raises
        ------
        - `ButtonNotFound`: The provided button was not found in the list of buttons on the menu
        """

    def remove_all_buttons(self) -> None:
        """Remove all buttons from the menu"""

    def disable_button(self, button: ViewButton) -> None:
        """Disable a button on the menu

        Parameters
        ----------
        button: :class:`ViewButton`
            The button to disable

        Raises
        ------
        - `ButtonNotFound`: The provided button was not found in the list of buttons on the menu
        """

    def disable_all_buttons(self) -> None:
        """Disable all buttons on the menu"""

    def enable_button(self, button: ViewButton) -> None:
        """Enable the specified button

        Parameters
        ----------
        button: :class:`ViewButton`
            The button to enable

        Raises
        ------
        - `ButtonNotFound`: The provided button was not found in the list of buttons on the menu
        """

    def enable_all_buttons(self) -> None:
        """Enable all buttons on the menu"""

    @ensure_not_primed
    def add_button(self, button: ViewButton) -> None:
        """Add a button to the menu

        Parameters
        ----------
        button: :class:`ViewButton`
            The button to add

        Raises
        ------
        - `MenuAlreadyRunning`: Attempted to call method after the menu has already started
        - `MenuSettingsMismatch`: The buttons custom_id was set as :attr:`ViewButton.ID_CUSTOM_EMBED` but the `menu_type` is :attr:`ViewMenu.TypeText`
        - `ViewMenuException`: The custom_id for the button was not recognized or a button with that custom_id has already been added
        - `TooManyButtons`: There are already 25 buttons on the menu
        - `IncorrectType`: Parameter :param:`button` was not of type :class:`ViewButton`
        """

    @ensure_not_primed
    def add_buttons(self, buttons: Sequence[ViewButton]) -> None:
        """Add multiple buttons to the menu at once

        Parameters
        ----------
        buttons: Sequence[:class:`ViewButton`]
            The buttons to add

        Raises
        ------
        - `MenuAlreadyRunning`: Attempted to call method after the menu has already started
        - `MenuSettingsMismatch`: One of the buttons `custom_id` was set as :attr:`ViewButton.ID_CUSTOM_EMBED` but the `menu_type` is :attr:`ViewMenu.TypeText`
        - `ViewMenuException`: The `custom_id` for a button was not recognized or a button with that `custom_id` has already been added
        - `TooManyButtons`: There are already 25 buttons on the menu
        - `IncorrectType`: One or more values supplied in parameter :param:`buttons` was not of type :class:`ViewButton`
        """

    def get_button(self, identity: str, *, search_by: Literal["label", "id", "name"] = ...) -> list[ViewButton]:
        """Get a button that has been registered to the menu by it's label, custom_id, or name

        Parameters
        ----------
        identity: :class:`str`
            The button label, custom_id, or name

        search_by: :class:`str`
            How to search for the button. If "label", it's searched by button labels. If "id", it's searched by it's custom_id.
            If "name", it's searched by button names

        Returns
        -------
        List[:class:`ViewButton`]: The button(s) matching the given identity

        Raises
        ------
        - `ViewMenuException`: Parameter :param:`search_by` was not "label", "id", or "name"
        """

    async def stop(
        self, *, delete_menu_message: bool = ..., disable_items: bool = ..., remove_items: bool = ...
    ) -> None:
        """|coro|

        Stops the process of the menu with the option of deleting the menu's message, removing the buttons, or disabling the buttons upon stop

        Parameters
        ----------
        delete_menu_message: :class:`bool`
            Delete the message the menu is operating from

        disable_items: :class:`bool`
            Disable the buttons & selects on the menu

        remove_items: :class:`bool`
            Remove the buttons & selects from the menu

        Parameter Hierarchy
        -------------------
        Only one option is available when stopping the menu. If you have multiple parameters as `True`, only one will execute
        - `disable_items` > `remove_items`

        Raises
        ------
        - `discord.DiscordException`: Any exception that can be raised when deleting or editing a message
        """

    @overload
    async def start(self, *, send_to: str | None = ..., reply: bool = ...) -> None: ...
    @overload
    async def start(self, *, send_to: int | None = ..., reply: bool = ...) -> None: ...
    @overload
    async def start(self, *, send_to: discord.TextChannel | None = ..., reply: bool = ...) -> None: ...
    @overload
    async def start(self, *, send_to: discord.VoiceChannel | None = ..., reply: bool = ...) -> None: ...
    @overload
    async def start(self, *, send_to: discord.Thread | None = ..., reply: bool = ...) -> None: ...
    @ensure_not_primed
    async def start(
        self,
        *,
        send_to: str | int | discord.TextChannel | discord.VoiceChannel | discord.Thread | None = ...,
        reply: bool = ...,
    ) -> None:
        """|coro|

        Start the menu

        Parameters
        ----------
        send_to: Optional[Union[:class:`str`, :class:`int`, :class:`discord.TextChannel`, :class:`discord.VoiceChannel`, :class:`discord.Thread`]]
                        The channel/thread you'd like the menu to start in. Use the channel/threads name, ID, or it's object. Please note that if you intend to use a channel/thread object, using
                        method :meth:`discord.Client.get_channel()` (or any other related methods), that channel should be in the same list as if you were to use `ctx.guild.text_channels`
                        or `ctx.guild.threads`. This only works on a context guild channel basis. That means a menu instance cannot be created in one guild and the menu itself (:param:`send_to`)
                        be sent to another. Whichever guild context the menu was instantiated in, the channels/threads of that guild are the only options for :param:`send_to`

            Note: This parameter is not available if your `method` is a :class:`discord.Interaction`, aka a slash command

        reply: :class:`bool`
            Enables the menu message to reply to the message that triggered it. Parameter :param:`send_to` must be :class:`None` if this is `True`. This only pertains to a non-interaction based menu.

        Raises
        ------
        - `MenuAlreadyRunning`: Attempted to call method after the menu has already started
        - `NoPages`: The menu was started when no pages have been added
        - `NoButtons`: Attempted to start the menu when no Buttons have been registered
        - `ViewMenuException`: The :class:`ViewMenu`'s `menu_type` was not recognized. There were more than one base navigation buttons. Or a :attr:`ViewButton.ID_CUSTOM_EMBED` button was not correctly formatted
        - `DescriptionOversized`: When using a `menu_type` of :attr:`ViewMenu.TypeEmbedDynamic`, the embed description was over discords size limit
        - `IncorrectType`: Parameter :param:`send_to` was not of the expected type
        - `MenuException`: The channel set in :param:`send_to` was not found
        """

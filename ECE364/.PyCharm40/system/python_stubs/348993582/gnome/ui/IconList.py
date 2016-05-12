# encoding: utf-8
# module gnome.ui
# from /usr/lib64/python2.6/site-packages/gtk-2.0/gnome/ui.so
# by generator 1.136
# no doc

# imports
import gnome.canvas as __gnome_canvas
import gobject as __gobject
import gobject._gobject as __gobject__gobject
import gtk as __gtk


class IconList(__gnome_canvas.Canvas):
    """
    Object GnomeIconList
    
    Signals from GnomeIconList:
      move-cursor (GtkDirectionType, gboolean)
      select-icon (gint, GdkEvent)
      unselect-icon (gint, GdkEvent)
      focus-icon (gint)
      text-changed (gint, gchararray) -> gboolean
      toggle-cursor-selection ()
    
    Signals from GnomeCanvas:
      draw-background (GdkDrawable, gint, gint, gint, gint)
      render-background (gpointer)
    
    Properties from GnomeCanvas:
      aa -> gboolean: Antialiased
        The antialiasing mode of the canvas.
      focused-item -> GnomeCanvasItem: focused-item
    
    Signals from GtkLayout:
      set-scroll-adjustments (GtkAdjustment, GtkAdjustment)
    
    Properties from GtkLayout:
      hadjustment -> GtkAdjustment: Horizontal adjustment
        The GtkAdjustment for the horizontal position
      vadjustment -> GtkAdjustment: Vertical adjustment
        The GtkAdjustment for the vertical position
      width -> guint: Width
        The width of the layout
      height -> guint: Height
        The height of the layout
    
    Signals from GtkContainer:
      add (GtkWidget)
      remove (GtkWidget)
      check-resize ()
      set-focus-child (GtkWidget)
    
    Properties from GtkContainer:
      border-width -> guint: Border width
        The width of the empty border outside the containers children
      resize-mode -> GtkResizeMode: Resize mode
        Specify how resize events are handled
      child -> GtkWidget: Child
        Can be used to add a new child to the container
    
    Signals from GtkWidget:
      composited-changed ()
      show ()
      hide ()
      map ()
      unmap ()
      realize ()
      unrealize ()
      size-request (GtkRequisition)
      size-allocate (GdkRectangle)
      state-changed (GtkStateType)
      parent-set (GtkWidget)
      hierarchy-changed (GtkWidget)
      style-set (GtkStyle)
      direction-changed (GtkTextDirection)
      grab-notify (gboolean)
      child-notify (GParam)
      mnemonic-activate (gboolean) -> gboolean
      grab-focus ()
      focus (GtkDirectionType) -> gboolean
      move-focus (GtkDirectionType)
      event (GdkEvent) -> gboolean
      event-after (GdkEvent)
      button-press-event (GdkEvent) -> gboolean
      button-release-event (GdkEvent) -> gboolean
      scroll-event (GdkEvent) -> gboolean
      motion-notify-event (GdkEvent) -> gboolean
      keynav-failed (GtkDirectionType) -> gboolean
      delete-event (GdkEvent) -> gboolean
      destroy-event (GdkEvent) -> gboolean
      expose-event (GdkEvent) -> gboolean
      key-press-event (GdkEvent) -> gboolean
      key-release-event (GdkEvent) -> gboolean
      enter-notify-event (GdkEvent) -> gboolean
      leave-notify-event (GdkEvent) -> gboolean
      configure-event (GdkEvent) -> gboolean
      focus-in-event (GdkEvent) -> gboolean
      focus-out-event (GdkEvent) -> gboolean
      map-event (GdkEvent) -> gboolean
      unmap-event (GdkEvent) -> gboolean
      property-notify-event (GdkEvent) -> gboolean
      selection-clear-event (GdkEvent) -> gboolean
      selection-request-event (GdkEvent) -> gboolean
      selection-notify-event (GdkEvent) -> gboolean
      selection-received (GtkSelectionData, guint)
      selection-get (GtkSelectionData, guint, guint)
      proximity-in-event (GdkEvent) -> gboolean
      proximity-out-event (GdkEvent) -> gboolean
      drag-leave (GdkDragContext, guint)
      drag-begin (GdkDragContext)
      drag-end (GdkDragContext)
      drag-data-delete (GdkDragContext)
      drag-failed (GdkDragContext, GtkDragResult) -> gboolean
      drag-motion (GdkDragContext, gint, gint, guint) -> gboolean
      drag-drop (GdkDragContext, gint, gint, guint) -> gboolean
      drag-data-get (GdkDragContext, GtkSelectionData, guint, guint)
      drag-data-received (GdkDragContext, gint, gint, GtkSelectionData, guint, guint)
      visibility-notify-event (GdkEvent) -> gboolean
      client-event (GdkEvent) -> gboolean
      no-expose-event (GdkEvent) -> gboolean
      window-state-event (GdkEvent) -> gboolean
      damage-event (GdkEvent) -> gboolean
      grab-broken-event (GdkEvent) -> gboolean
      query-tooltip (gint, gint, gboolean, GtkTooltip) -> gboolean
      popup-menu () -> gboolean
      show-help (GtkWidgetHelpType) -> gboolean
      accel-closures-changed ()
      screen-changed (GdkScreen)
      can-activate-accel (guint) -> gboolean
    
    Properties from GtkWidget:
      name -> gchararray: Widget name
        The name of the widget
      parent -> GtkContainer: Parent widget
        The parent widget of this widget. Must be a Container widget
      width-request -> gint: Width request
        Override for width request of the widget, or -1 if natural request should be used
      height-request -> gint: Height request
        Override for height request of the widget, or -1 if natural request should be used
      visible -> gboolean: Visible
        Whether the widget is visible
      sensitive -> gboolean: Sensitive
        Whether the widget responds to input
      app-paintable -> gboolean: Application paintable
        Whether the application will paint directly on the widget
      can-focus -> gboolean: Can focus
        Whether the widget can accept the input focus
      has-focus -> gboolean: Has focus
        Whether the widget has the input focus
      is-focus -> gboolean: Is focus
        Whether the widget is the focus widget within the toplevel
      can-default -> gboolean: Can default
        Whether the widget can be the default widget
      has-default -> gboolean: Has default
        Whether the widget is the default widget
      receives-default -> gboolean: Receives default
        If TRUE, the widget will receive the default action when it is focused
      composite-child -> gboolean: Composite child
        Whether the widget is part of a composite widget
      style -> GtkStyle: Style
        The style of the widget, which contains information about how it will look (colors etc)
      events -> GdkEventMask: Events
        The event mask that decides what kind of GdkEvents this widget gets
      extension-events -> GdkExtensionMode: Extension events
        The mask that decides what kind of extension events this widget gets
      no-show-all -> gboolean: No show all
        Whether gtk_widget_show_all() should not affect this widget
      has-tooltip -> gboolean: Has tooltip
        Whether this widget has a tooltip
      tooltip-markup -> gchararray: Tooltip markup
        The contents of the tooltip for this widget
      tooltip-text -> gchararray: Tooltip Text
        The contents of the tooltip for this widget
      window -> GdkWindow: Window
        The widget's window if it is realized
      double-buffered -> gboolean: Double Buffered
        Whether or not the widget is double buffered
    
    Signals from GtkObject:
      destroy ()
    
    Properties from GtkObject:
      user-data -> gpointer: User Data
        Anonymous User Data Pointer
    
    Signals from GObject:
      notify (GParam)
    """
    def append(self, *args, **kwargs): # real signature unknown
        pass

    def append_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def find_icon_from_filename(self, *args, **kwargs): # real signature unknown
        pass

    def focus_icon(self, *args, **kwargs): # real signature unknown
        pass

    def freeze(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_at(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_data(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_filename(self, *args, **kwargs): # real signature unknown
        pass

    def get_icon_text_item(self, *args, **kwargs): # real signature unknown
        pass

    def get_items_per_line(self, *args, **kwargs): # real signature unknown
        pass

    def get_num_icons(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection(self, *args, **kwargs): # real signature unknown
        pass

    def get_selection_mode(self, *args, **kwargs): # real signature unknown
        pass

    def icon_is_visible(self, *args, **kwargs): # real signature unknown
        pass

    def insert(self, *args, **kwargs): # real signature unknown
        pass

    def insert_pixbuf(self, *args, **kwargs): # real signature unknown
        pass

    def moveto(self, *args, **kwargs): # real signature unknown
        pass

    def remove(self, *args, **kwargs): # real signature unknown
        pass

    def select_all(self, *args, **kwargs): # real signature unknown
        pass

    def select_icon(self, *args, **kwargs): # real signature unknown
        pass

    def set_col_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def set_hadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_border(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_data(self, *args, **kwargs): # real signature unknown
        pass

    def set_icon_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_row_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def set_selection_mode(self, *args, **kwargs): # real signature unknown
        pass

    def set_separators(self, *args, **kwargs): # real signature unknown
        pass

    def set_text_spacing(self, *args, **kwargs): # real signature unknown
        pass

    def set_vadjustment(self, *args, **kwargs): # real signature unknown
        pass

    def thaw(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_all(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_icon(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __iter__(self): # real signature unknown; restored from __doc__
        """ x.__iter__() <==> iter(x) """
        pass

    __gtype__ = None # (!) real value is ''


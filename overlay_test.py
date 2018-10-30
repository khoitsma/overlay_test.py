# credit: github.com/mikaelho/pythonista-gestures
# credit: github.com/jsbain/viewbrowser

from overlay import Overlay, AppWindows
from gestures import Gestures
import ui

if __name__=='__main__':
    
    
    #view = ui.View(name='Hello')
    #view.frame = (0, 0, 240, 240)
    #view.flex = 'WH'
    #view.background_color = 'white'
    
    
    iv0=ui.ImageView(frame=(0,0,300,300))
    iv0.image=ui.Image.named('test:Peppers')
    iv0.name='OMAIN▪️'
    
    
    iv1=ui.ImageView(frame=(0,0,200,200))
    iv1.image=ui.Image.named('foo.png')
    iv1.name='ICR▪️'
    iv1.alpha=1
    overlay1=Overlay(content=iv1,parent=AppWindows.root())
    overlay1.content_view.border_width=2
    iv1.border_width=1
    iv1.content_mode=ui.CONTENT_SCALE_ASPECT_FIT
    
    
    iv2=ui.ImageView(frame=(0,0,200,200))
    iv2.image=ui.Image.named('fooe.png')
    iv2.name='E▪️'
    iv2.alpha=1
    overlay2=Overlay(content=iv2,parent=AppWindows.root())
    overlay2.content_view.border_width=2
    iv2.border_width=1
    iv2.content_mode=ui.CONTENT_SCALE_ASPECT_FIT
    
    
    omain=Overlay(name='abc', content=iv0, parent=AppWindows.root())
    omain.content_view.border_width=2
    iv0.border_width=1
    iv0.content_mode=ui.CONTENT_SCALE_ASPECT_FIT

<div id="top"></div>

<br/>
<div align="center">
  <a href="https://github.com/BornPaster/bruce">
    <img src="https://i.imgur.com/wa8n82V.png" alt="Logo" >
  </a>
  
  <h2 align="center">Bruce™</h3>

  <p align="center">
    A very sleek, modern, and monochrome style logger modification.
    <br />
    <br />
    <a href="https://github.com/BornPaster/bruce/issues">Report Bug</a>
    ·
    <a href="https://github.com/BornPaster/bruce/issues">Request Feature</a>
  </p>
</div>


---------------------------------------

### Requirements
* Windows OS

---------------------------------------

### Usage

```python 
from bruce import init, bracks, bruceformatter
import logging

init()

logger = logging.getLogger("bruce-demo")
handler = logging.StreamHandler()
handler.setFormatter(bruceformatter("%(levelname)s: %(message)s"))
logger.addHandler(handler)
logger.setLevel(logging.INFO)

logger.info(f"this is a test log! {bracks('test brackets')}")
```

---------------------------------------

### Notes
* can be used for anything including tools, api, etc.
* very clean and super sleek so its actually good to look at.
* star the repo if you end up liking what you see <3

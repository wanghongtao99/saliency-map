saliency-map (Python)
============
Saliency Map. Laurent Itti, Christof Koch (2000)


```
from saliency_map import SaliencyMap
from utils import OpencvIo

oi = OpencvIo()
src = oi.imread(IMAGE_PATH)
sm = SaliencyMap(src)
oi.imshow_array([sm.map])
```

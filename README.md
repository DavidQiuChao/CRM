# CRM
This project aims at throughly understand the implementation detail of paper "A New Low-Light Image Enhancement Algorithm using Camera Response Model",ICCV2017. The original project,[OpenCE](https://github.com/baidut/OpenCE),is implemented by Matlab. Since the project is reproduced by python, some key function cannot be reproduced accuratly. If you find this project helpfully and has some advices,please feel free to contact me.

# How to use the code
Just run the command "python main.py -i 'dataPath'". The variable "dataPath" specifies the testing data path.

# Testing Result
input image|official illumMap|our illumMap|official result|our result
----|----|----|----|----
![13](https://github.com/DavidQiuChao/CRM/blob/main/figs/13.jpg)|![oilu13](https://github.com/DavidQiuChao/CRM/blob/main/figs/illuM13.jpg)|![milu13](https://github.com/DavidQiuChao/CRM/blob/main/figs/illum_13.jpg)|[or13](https://github.com/DavidQiuChao/CRM/blob/main/figs/pp_13.jpg)|[mr13](https://github.com/DavidQiuChao/CRM/blob/main/figs/my_13.jpg)
![36](https://github.com/DavidQiuChao/CRM/blob/main/figs/36.jpg)|![oilu36](https://github.com/DavidQiuChao/CRM/blob/main/figs/illuM36.jpg)|![milu36](https://github.com/DavidQiuChao/CRM/blob/main/figs/illum_36.jpg)|[or36](https://github.com/DavidQiuChao/CRM/blob/main/figs/pp_36.jpg)|[mr36](https://github.com/DavidQiuChao/CRM/blob/main/figs/my_36.jpg)
![37](https://github.com/DavidQiuChao/CRM/blob/main/figs/37.jpg)|![oilu37](https://github.com/DavidQiuChao/CRM/blob/main/figs/illuM37.jpg)|![milu37](https://github.com/DavidQiuChao/CRM/blob/main/figs/illum_37.jpg)|[or37](https://github.com/DavidQiuChao/CRM/blob/main/figs/pp_37.jpg)|[mr37](https://github.com/DavidQiuChao/CRM/blob/main/figs/my_37.jpg)


# CRM
This project aims at throughly understand the implementation detail of paper "A New Low-Light Image Enhancement Algorithm using Camera Response Model",ICCV2017. The original project,[**OpenCE**](https://github.com/baidut/OpenCE),is implemented by Matlab. Since the project is reproduced by python, some key function cannot be reproduced accuratly. If you find this project helpfully and have some advices,please feel free to contact me.

## How to use the code
Just run the command "python main.py -i 'dataPath'". The variable "dataPath" specifies the testing data path.

## Difference
For estimating the exposure ratio map, the original project uses the Matlab function, [**Precondition Conjugate Gradient**](https://www.mathworks.com/help/matlab/ref/pcg.html) and [**Incomplete Cholesky Decomposition**](https://ww2.mathworks.cn/help/matlab/ref/ichol.html?requestedDomain=cn.mathworks.com), to solve the linear equation system. But in this code, the [**Conjugate-Gradient**](https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.cg.html#scipy.sparse.linalg.cg) is uesd to solve the linear problems. And the "CG" function in Scipy takes more time than "PCG" function in Matlab.

## Testing Result
input image|official result|our result|official illumMap|our illumMap
----|-----|------|-------|--------
![13](https://github.com/DavidQiuChao/CRM/blob/main/figs/13.jpg)|![or13](https://github.com/DavidQiuChao/CRM/blob/main/figs/pp_13.jpg)|![mr13](https://github.com/DavidQiuChao/CRM/blob/main/figs/my_13.jpg)|![oilu13](https://github.com/DavidQiuChao/CRM/blob/main/figs/illuM13.jpg)|![milu13](https://github.com/DavidQiuChao/CRM/blob/main/figs/illum_13.jpg)
![36](https://github.com/DavidQiuChao/CRM/blob/main/figs/36.jpg)|![or36](https://github.com/DavidQiuChao/CRM/blob/main/figs/pp_36.jpg)|![mr36](https://github.com/DavidQiuChao/CRM/blob/main/figs/my_36.jpg)|![oilu36](https://github.com/DavidQiuChao/CRM/blob/main/figs/illuM36.jpg)|![milu36](https://github.com/DavidQiuChao/CRM/blob/main/figs/illum_36.jpg)
![37](https://github.com/DavidQiuChao/CRM/blob/main/figs/37.jpg)|![or37](https://github.com/DavidQiuChao/CRM/blob/main/figs/pp_37.jpg)|![mr37](https://github.com/DavidQiuChao/CRM/blob/main/figs/my_37.jpg)|![oilu37](https://github.com/DavidQiuChao/CRM/blob/main/figs/illuM37.jpg)|![milu37](https://github.com/DavidQiuChao/CRM/blob/main/figs/illum_37.jpg)


# 4D-RADAR 

### 1. Execution Environment

|    |Environment   |
|----|-------:|
|OS|Ubuntu 20.04/22.04|
|Python|Python 3.10|
|ROS|ROS2 foxy, humbel|

------------------
### 2. Installation

1. Ubuntu (20.04/22.04)
2. ROS2 ([foxy](https://docs.ros.org/en/foxy/Installation.html)/[humbel](https://docs.ros.org/en/humble/index.html))

------------------
### 3. Excution

#### 1. Clone the repository
```cmd
$ git clone https://github.com/hrin-yoon/4D-RADAR.git
$ cd 4D-RADAR
```

#### 2. Setting
![ROS_WORK-페이지-3 drawio](https://github.com/user-attachments/assets/34242393-fef3-4942-9b05-470116246363)
- Befor multi pc excute,we need to set each PC using [DDS](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0_%EB%B6%84%EC%82%B0_%EC%84%9C%EB%B9%84%EC%8A%A4)

```cmd
##### PC1 & PC2 
$ export ROS_DOMAIN_ID=5
$ echo "export ROS_DOMAIN_ID=5" >> ~/.bashrc 
$ source ~/.bashrc

$ export ROS_LOCALHOST_ONLY=0
$ echo "export ROS_LOCALHOST_ONLY=0" >> ~/.bashrc 
$ source ~/.bashrc
```

#### 3. Excute 
##### < Single PC communocattion >
![ROS_WORK-페이지-3 drawio (1)](https://github.com/user-attachments/assets/3f5c8a70-8e20-4a1a-ab6c-f7bb8b62d6cb)
-  You don't need to configure the 2. setting if you're using a single PC.
-  If you want to communicate using a single PC, you need to open 4 terminals (4 on PC1).

```cmd
$ python3 psudo_radar.py # terminal 1
$ python3 perception.py # terminal 2

$ rviz2 #terminal 3
$ rqt_graph # terminal 4
```
##### < Multi PC communication >
![ROS_WORK-페이지-3 drawio (2)](https://github.com/user-attachments/assets/5bd20ddc-1462-4bb9-96b6-b0193032868d)
- If you are using multiple computers, each computer will require its own configuration. We'll use communication between two PCs as an example.
- To communicate between two PCs, you need to open 4 terminals (1 on PC1 and 3 on PC2).
  
```cmd
$ python3 psudo_radar.py # terminal 1 in PC1
$ python3 perception.py # terminal 2 in PC2

$ rviz2 #terminal 3 in PC2
$ rqt_graph # terminal 4 in PC2
```
------------------
### 4. Expected result

#### RVIZ2 excuting result
[Screencast from 08-28-2024 05:15:29 PM.webm](https://github.com/user-attachments/assets/9b76decd-96f8-4641-a394-12305c022ce0)

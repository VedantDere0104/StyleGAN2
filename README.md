# StyleGAN2
Pytorch Implementation of StyleGAN2

Original Implementation :- https://github.com/rosinality/stylegan2-pytorch

StyleGAN2 version which is compatible on CPU as well as GPU

## Requirements 

To run it on local system :-
Clone the Repo 

```
cd StyleGAN2
```

```
pip install -r requirements.txt
```

I would suggest to run this project in nvidia pytorch docker .

```
docker pull nvcr.io/nvidia/pytorch:21.12-py3
```

When the download is complete then you can use run command to fire the docker container .

```
docker run --gpus all -it --rm -v local_dir:container_dir nvcr.io/nvidia/pytorch:xx.xx-py3
```

## Usage

Download the pretrained weights for StyleGAN2 from https://drive.google.com/open?id=173WmV5EhFfMQTeDpYkLAJi3qhPtZOQs5

To generate fake images using some random latent code 

```
python test.py 
```

## Train

To train model from scratch you need to arange dataset as follows

|── dataset                  
│   ├── 1.png             
│   ├── 2.png             
│   ├── 3.png             
│   ├── 4.png            
│   └── ...                
└── ...

```
python train.py --path {path to the dataset foler} --iter {Total number of epochs} --batch {batch size}
```
for more arguments like wandb refer train.py 


## Results
file![000000](https://user-images.githubusercontent.com/76057253/147431574-a30c7fbb-139b-46af-836e-2c2fde5009f4.png)

![000001](https://user-images.githubusercontent.com/76057253/147431605-5c858176-f22b-4735-af9c-72cbd362ebca.png)




![000019](https://user-images.githubusercontent.com/76057253/147431730-0e1ce747-cd13-42fc-b2aa-cd636c87cd71.png)
![000007](https://user-images.githubusercontent.com/76057253/147431737-4de6e05f-063c-4faa-bc70-19a2e258a3b1.png)


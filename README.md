# SMART DASH CAM

A dash-cam that detects and classifies cars using transfer learning models, computer vision, TensorFlow, and Python.

![Copy of IMG_0639](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/025f5113-635a-4d82-87f8-0c9756188dc8)

## Yolonet
We used Yolonet and trained it against many images of cars in order to detect a car in the camera's feild of vision. The camera takes a snapshot of this car and processes it using MobileNet.
![Yolonet](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/0975a5cb-8ac7-4dd0-9a8a-37334c40764b)

## MobileNet
We used a dataset of 10 different cars with an extensive amount of pictures for each car to train the model. 
![image](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/0078277b-8d54-4e48-bc57-5c583531e538)
Our goal was to hit at least 92% confidence for our model when testing against images of cars that weren't in the dataset. We used an Acura Integra to test the model.
![Directory3](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/308f9648-e4d1-4f27-9f0c-7eac136f624d)


## Testing
We dispayed the accuracy of the model using this confusion matrix. The model got all cars correct after 15 epochs, surpassing our goal with a confidence rating of 96%. The project was ready to be scaled up.
![Confusion Matrix](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/e28e4015-6717-4a16-985d-8f8134af46c1)

## User Interface
Here is the final User Interface with touch screen functionality. When a car is selected, the device snap shots the image frame and processes it to determine if the selected car was found.
![User Interface](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/1bb62e92-b10b-4cc3-b97f-0ac506cb56cc)

## Frame
We used a tissue box to house the components of the device while building the software's functionality. 
![Tissue Box Frame](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/72844c9f-0685-4df8-89b9-8bea3315e336)

A final frame design for the device was built using Solidworks CAD.
![FinalFrame2](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/19a9e831-5496-4774-9c8e-5d905067e0fb)
![FinalFrame1](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/cd115cbf-28db-428f-8d9c-ad36ff5f8015)

We 3D printed at the UIC Engineering Makerspace and assembled the final prototype.
![Dash Cam Frame Draft](https://github.com/Sean-Conrad/Smart-Dash-Cam/assets/98624752/728e1a08-7f94-4268-86d0-4ea22cb11215)

## Conclusion
The AI-dashcam was finally completed and met nearly all of the objectives that we
planned out. We were able to build a device that takes in live images, processes any cars in those images,
and accurately identify those cars using a trained model. We optimized the model by testing different
parameters and dataset configurations, and were able to exceed our engineering goal of 92% accuracy.
Additionally,  we were able to successfully integrate multiple modules to the NVIDIA Jetson Nano, and
tied up all the components into a compact device using Solidworks. This included a GPS Module, a Wifi antenna,
a camera Module, and a large touch screen display. Furthermore, our device not only exhibitted connection between
multiple hardware peripherals but through software as well. We designed a user interface with touch screen 
compatibility, live camera viewing, and dynamic rendering of results, offering an intuitive way for users to 
interact with the device. While we had great success in these departments, a few improvements could have been 
made to the device. The software expereinced significant lag when ran on the prototype as opposed to a desktop 
computer. This can be improved by rewriting the program in C in order to utilize TensorFlow's lightweight version 
for mobile models. Additionally, using the newer version of the Jetson Nano with 2 extra GB of memory would 
further optimize the runtime. Minor tweaks to the User Interface implementation, and more effective abstraction 
of program functionsmay help as well. All in all, this project exemplifies the core beauty of computer engineering, 
marrying the _physicalality_ of Electrical Hardware, the _intentionality_ of Computer Aided Design, the _abstract_ 
in UI and Software, and _innovation_ through novel concepts in Machine Learning.


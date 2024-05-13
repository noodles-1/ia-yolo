# Image-Adaptive YOLO for CSGO Thesis LPR System
#### This repository is based on wenyyu's [Image-Adaptive YOLO](https://github.com/wenyyu/Image-Adaptive-YOLO).
#### Academic paper available on [arxiv](https://arxiv.org/abs/2112.08088)

The repository has been reconfigured to meet the [LPR system's](https://github.com/noodles-1/csgo-system) requirements.

Image-Adaptive YOLO models (foggy and lowlight) were trained over 100 epochs on Philippine license plate datasets: [ANPR](https://universe.roboflow.com/thesis-u0tkq/anpr-ver79), [KNN](https://universe.roboflow.com/2014-series-license-plate/knn-brxiq), [OTSU](https://universe.roboflow.com/adrian-dumaop/otsu), [Plate](https://universe.roboflow.com/university-of-the-cordilleras-ezcii/plate-tuigx), and [UE Parking](https://universe.roboflow.com/ue-parking/ue-parking-eutbc).

CNN-PP and DIP modules were preserved as a basis for optimal preprocessing for the license plate recognition, and YOLOv3 object detection is ignored, and will be substituted by the trained YOLOv8 license plate detection model.

This system runs on WSL Ubuntu 22.04.3. Refer to `requirements.txt` for correct package versions.
# System Design

## Goal of the system

The main goal of this program is to design a simple application for editing video (that is more than a few video to fit together and make simple synchronization).

Our ultimate goal is to make a video editing software similar to Adobe Premiere Pro or Final Cut Pro.

## Project plan

## Business process model

## Requirements

## Functional plan

## Physical enviorement

## Architectural plan

## Implementation plan

## Testing plan

We plan to use CI (continuous integration) to automatically run test at each Commit and merge.

## Install plan

We will publish the package to [PyPi](https://pypi.org/) when it is ready.

Then the user can download and install it by `pip`:

```shell
pip install video_creator
```

Developers can get the source code via Clone our Git Repo:

```shell
git clone git@github.com:SDM-2021-16-SpongeBob/video_creator.git
```

## Maintenance plan
 Following are the content of software development plan:

 -Processes:

    Typically, this would include your Software Development, Risk Management, Usability and Problem Resolution processes.

 -Required Resources:   
    
     Next, talk about the technical resources you need. At the minimum, you need a compiler or a runtime (e.g. CPython 3.8). You’ll probably also have some sort of IDE software.

 -Configuration Management:

     Describe how you do configuration management. Wait, what’s that? That’s simply what sort of version control software you use (I’d guess it’s git), how you name versions and how you create branches / merges during development.   

 -Verification Activities: 

     Software verification is yet another vague term, but for practical purposes, let’s just say that that refers to “code review” in human language.

## Project plan
 
When I started my deep learning journey, one of the first things I learned was image classification. It’s such a fascinating part of the computer vision fraternity 
and I was completely immersed in it! But I have a curious mind and once I had a handle on image classification, I wondered if I could transfer that learning to videos.
Was there a way to build a model that automatically identified specific people in a given video at a particular time interval? Turns out, there was and I’m excited to share my approach with you!

For example: We have a different image(e.g shark) on each page of the book, and as we flip these pages, we get an animation of a shark dancing. You could even call it a kind of video. The visualization gets better the faster we flip the pages. In other words, this visual is a collection of different images arranged in a particular order.

Similarly, videos are nothing but a collection of a set of images. These images are called frames and can be combined to get the original video. So, a problem related to video data is not that different from an image classification or an object detection problem. There is just one extra step of extracting frames from the video.

Let me first summarize the steps we will follow in this:

Import and read the video, extract frames from it, and save them as images.
Label a few images for training the model.
Build our model on training data.
Make predictions for the remaining images.
Calculate the screen time of both. 

## Business process model


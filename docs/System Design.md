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

- For example: 
We have a different image(e.g shark) on each page of the book, and as we flip these pages, we get an animation of a shark dancing. You could even call it a kind of video. The visualization gets better the faster we flip the pages. In other words, this visual is a collection of different images arranged in a particular order.

Similarly, videos are nothing but a collection of a set of images. These images are called frames and can be combined to get the original video. So, a problem related to video data is not that different from an image classification or an object detection problem. There is just one extra step of extracting frames from the video.

- Let me first summarize the steps we will follow in this:

1. Import and read the video, extract frames from it, and save them as images.
2. Label a few images for training the model.
3. Build our model on training data.
4. Make predictions for the remaining images.
5. Calculate the screen time of both. 

## Business process model

Business process maodeling is a way to visualize what a business does by taking into account roles, responsibilities and standards. Business process modeling (BPM) takes this one step further by providing a visual way to understand, analyze, and improve upon a current method of working. Business process modeling is more about in-depth analysis and optimizing inefficiencies and bottlenecks.

- Basic Components of Business Process Modeling:

1. Process:  The overall workflow from a starting point to its successful completion.
2. Tasks or Activities: Something performed by a person or a system.
3. Flows: This is indicated on the process map by connecting lines and arrows.
4. Events: These are triggers that cause a process to begin, end, or may redirect a process to a different path.
5. Gateways: Decisions that can change the path of the process depending on conditions or events.
6. Participants: Specifically naming the people or systems that perform the tasks or activities.

- How to Make a Business Process Model:

1. Identify the process you want to document
2. Gather information from process participants via interviews or observations
3. Identify the start and end points of your process
4. Break the process into distinct tasks and decision points

- Explaination:

To present a business process model, some people like to play a slideshow on projector and explain it with the help of a laser pen. 
Others may like to open up diagrams directly in Visual Paradigm and walk (scroll) through the diagram manually with the mouse pointer. 
Either way, it comes with a bit of rigidity.

Whether you are reading a business process diagram in Visual Paradigm, slideshow, handout or from projector, you are actually studying something dynamic from static image. The process is not running in the image itself, but in your brain. For this reason, it can be limited to how much you can learn from these static representation of workflows. Moreover, you may easily miss out possible process flows for complex processes or processes that involve many conditional flows.

- For Example:

Let’s begin our BPM with a rather simple process:

When naming tasks, we try to adhere to the object-orientated design principle of using the [verb] + [object] pattern. We would say “acquire groceries,” for example, not “first take care of shopping for groceries.”
Events refer to something that has already happened regardless of the process (if they are catching events) or as a result of the process (if they are throwing events). For this reason, we use the [object] and make the [verb] passive in voice, so we write “hunger noticed.” BPM does not require you to model start and end events for a process – you can leave them out, but if you model a start event, you must model an end event for each path. The same is true for end events, which require start events. We always create our models with start and end events for two reasons: first, that way it’s possible to determine the process trigger, and second, you can describe the final status of each path end. We only sometimes abandon this practice with sub-processes.

## Functional plan

1. Add watermark to video(s) [option to choose size & position of watermark]
2. Create gif from video(s) [option to choose size, type & start/endtime of gif]
3. Cut video(s) in to multiple parts
4. Export audio from video(s)
5. Make snapshots from video(s)
6. Multiprocessing for every feature to speed up process time






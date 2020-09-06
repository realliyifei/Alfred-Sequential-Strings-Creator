<h1 align="center">
  <img src="./icon.png" width="128" height="128">
</h1>

# Sequential Strings Creator (Mac Alfred Workflow)

This simple workflow lets you create a series of sequential strings, horizontally or vertically. Useful in todo apps, note-taking apps, etc.

<h1 align="center">
  <img src="./gifs/SequentialStrings_Demo_Notes.gif"  width="400">
</h1>

## Examples

It supports the sequence of either integer or one-digit float.

The input format is `strings {number-number} strings`, where curly braces work as determinators.

* Type `hw{1-3} ` after trigger keyword, and choose *horizontally*, it creates:

    ```
    hw1 hw2 hw3
    ```

* Type `section {1.8-2,2}, ` after trigger keyword, and choose *horizontally*, it creates:
    
    ```
    section 1.8, section 1.9, section 2.0, section 2.1, section 2.2
    ```

* Type `chapter {12-15} today` after trigger keyword, and choose *vertically*, it creates: 

    ```
    chapter 12 today
    chapter 13 today
    chapter 14 today
    chapter 15 today
    ```

## More Demos

It's also helpful when intergrating with other apps. 

We can create a series of tasks in todo apps like `Things 3` quickly.

<h1 align="center">
  <img src="./gifs/SequentialStrings_Demo_Things.gif" width="400">
</h1> 

We can create a series of headers of the table in the note-taking apps like `OneNote` conveniently.

<h1 align="center">
  <img src="./gifs/SequentialStrings_Demo_OneNote.gif" width="400">
</h1>

The possibility is ***unlimited***!

---

## Install this workflow

Simply donwload the [alfredworkflow file](https://github.com/yli/Alfred-Sequential-Strings-Creator/blob/master/Sequential_Strings_Creator.alfredworkflow) and then open it to import to the alfred.

## Software: Alfred (Mac)

![Alfred Logo](https://i.pinimg.com/originals/5c/23/a6/5c23a6723d3b19e892985fd918cf0aab.png)

The software can be downloaded [here](https://www.alfredapp.com/). You need to [buy the Powerpack](https://buy.alfredapp.com/) to use this workflow.

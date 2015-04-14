# Civil Discourse

The website designed to facilitate arguments on the internet (everybody's favourite pasttime).

The website uses [web2py](http://www.web2py.com/) and tries to adhere to the [MVC architectural pattern](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller). 
The controllers are the in the `controllers` folder. The views are in the `views` folder. The models are in the `models` folder. 
To stop the views getting a bit too crazy with python code, there are some helper methods that are in the `modules` folder.

The `languages` folder holds translations that I have not done yet. At the moment it just holds whatever the default translations are that come with web2py. 
I have, however, tried to [internationalise](https://en.wikipedia.org/wiki/Internationalization_and_localization) the site throughout, so if there are people who would like to translate it, it should be a very simple matter of editing the python files (which just contain python dictionaries) in the `languages` folder.

The `static` folder holds both CSS and Javascript for the site, as well as (as of yet untouched) error pages, like 404 and 500.
The CSS uses a big load of styles I've compiled and for some reason called [puff.css](https://github.com/IMP1/civil-discourse/blob/master/static/css/puff.css). 
There's also some Civil Discourse site-specific CSS in the files beginning with `cd`. CSS that's common across the whole site goes in `cd.css`, and CSS that's specific to a page or two goes in its own file.

If you have any issues with the site as a website, rather than as a forum for discussion, feel free to [create an issue](https://github.com/IMP1/civil-discourse/issues) about it (if you have problems with the latter, create a discussion on the site about it!).
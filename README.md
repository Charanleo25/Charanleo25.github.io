# How to Build a Chat App

![](/projects/chat-app/guideAssets/final.png)

> - 🧑‍💻 [You will build this](https://app.qoom.io/~/projects/chat-app/chat)
> - ▶️ [Tutorial Video](https://youtu.be/tnsqo4hwutg)
> - 🗂️ Source Files
>	- [index.html](https://app.qoom.io/edit/projects/chat-app/chat/index.html)


## What you will get from this workshop
1. A great [starting app](#starterapp) you can use to make your own private chat application
2. A [list of resources](#listofresources) for further help and continued learning


## About the project

In this workshop you will learn how to build and customize a private chat application

While building this app you will learn how to do the following:
 - HTML
	- **Mobile Layout** &rArr; Creating web app that is laid out for a mobile device
 - CSS 
	- **Flex Box** &rArr; More practice using flex box to make sure things are centered inside of elemets.
	- **Grid System** &rArr; More practice using the grid system to make sure things are laided out aesthetically
 - Javascript:
	- **Importing 3rd party libraries** &rArr; Building off of tools built from others so that you can focus on building what you need
	- **Sockets** Using sockets to communicate with other people using other browsers on other devices

## Creating your account

1. Go to <https://www.qoom.io>
2. Click the `Sign Up` button
3. Follow the instructions

***

## `HTML`: Creating our Web App Layout

Copy the following HTML:

```html
<body>
	<header>
		<h1>🔒 Private Chat </h1>
	</header>
	<main>
		<div class='you'>Welcome!</div>
		<div class='me'></div>
	</main>
	<footer>
		<textarea placeholder='Type your message here...'></textarea>
		<button>Send</button>
	</footer>
</body>
```

In this HTML page we used the `Semantic` elements to describe our layout. The `main` section will hold the messages and the `footer` section will be where the user enters their messages.


> **Exercise**:
> - Change the text in the `h1` element.

Adding a `title` element so that your app has an title in the tab:
```html
<head>
	<title>🔒 Private Chat</title>
</head>
```


***

## `CSS`: Styling our Web App

Now lets use the `Flex` and `Grid` Systems to make everything lay out nicely

```html
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link href="https://fonts.googleapis.com/css2?family=Inconsolata&family=Fredericka+the+Great&family=Mali&display=swap" rel="stylesheet">
	<title>Private Chat</title>
	<style>
		* {
			box-sizing:border-box;
			margin:0;
			padding:0;
		}
		body {
			display:grid;
			grid-template-rows: 64px auto 100px;
			grid-template-columns: auto 600px auto;
			width:100vw;
			height:100vh;
			overflow: hidden;
			font-family: system-ui, san-serif;
			background-color: #fcd411;
		}
		header {
			grid-column-start: 2;
			grid-column-end: 3;
			text-align:center;
			display:flex;
			align-items:center;
			justify-content:center;
			background-color: #2e2e30;
			color: #fcd411;
		}
		header > h1 {
			font-family: 'Fredericka the Great', cursive;
			font-size: 2em;
		}
		main {
			grid-column-start: 2;
			grid-column-end: 3;
			list-style:none;
			padding: 24px;
			display:flex;
			flex-direction:column;
			align-items:center;
			justify-content:flex-start;	
			background-color: white;
			overflow-y: auto;
			overflow-x: hidden;
		}
		main > div {
			width: 100%;
			font-size: 18px;
			margin: 8px 0;
		}
		main > div.me {
			font-family: 'Mali', cursive;
			text-align: right;
		}
		main > div.you {
			font-family: 'Inconsolata', monospace;
			text-align:left;
		}
		footer {
			grid-column-start: 2;
			grid-column-end: 3;
			display:grid;
			grid-template-columns: auto 80px;
			background-color: #fcd411;
		}
		footer > textarea {
			font-family: 'Mali', cursive;
			font-size: 18px;
			padding: 8px 16px;
			resize: none;
		}
		footer > button {
			font-family: 'Fredericka the Great', cursive;
			font-size: 20px;
			background-color: #fcd411;
		}
		@media only screen and (max-width: 768px) {
			body {
				height: calc(100vh - 114px);
				grid-template-columns: auto 100% auto;
			}
		}
	</style>
</head>
```

> **Exercise**:
> - Change the fonts using Google Fonts <https://fonts.google.com/>
> - Change the colors

***

## `Javascript`: Creating a socket connection with other browsers

Since we are using `sockets` we will need to import the library that makes this easy. Please add the following code at the bottom of the `head` element:
```html
<script src='/libs/socketio.js'></script>
```

Then we can initialize the socket connections using the following function:
```html
<script src='/libs/socketio.js'></script>
<script type='module'>
	
	// Creating a socket variable to talk to our server with
	const socket = io('/tunnel');
	
	async function initializeSockets() {
	
		// Telling our webserver to create a `chat` channel to talk with other browsers with
		const res = await fetch('/tunnel/register', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json'
			},
			body: JSON.stringify({
				events: ['chat']
			})
		});
		
		// Waiting for our server to respond
		const resp = await res.json();
	
		// Handle any errors from our server
		if(resp.error) return alert(resp.error)
		
		// Define what to do when someone sends us a message
		socket.on('chatresponse', function(data) {
			
		});
		
		// Define what to do when someone joins the chat room
		socket.on('userconnected', (socketId) => {
			console.log('userconnected: ' + socketId);
		});
		
		// Define what to do when someone leaves the chat room
		socket.on('userdisconnected', (socketId) => {
			console.log('disconnected: ' + socketId);
		})

	}
	
	// Initializing the socket connection
	initializeSockets();
</script>
```

> **Exercise**:
> - Open up the webpage you created and open up `Dev Tools` by right clicking and selecting `Inspect`
> - Send the webpage to someone else
> - See in the `console` when someone joins

***

## `Javascript`: Asking for the name of the person joining the chat

In the `script` tag created above add the following code at the top:

```javascript
// Checks `localStorage` if the person name is saved
let name = localStorage.getItem('name');

// If no name is found, ask the user for their name and save it
if(!name) {
	name = prompt("What is your name?")
	localStorage.setItem('name', name);
}
```

> **Exercise**:
> - Test it
> - Go to the `storage` tab in the `Dev Tools` and see the data saved in `localStorage`

***

## `Javascript`: Displaying the chat messages

At the bottom of the `script` tag created above add the following code:

```javascript
// Putting all the elements into variables
const $button = document.querySelector('button');
const $textarea = document.querySelector('textarea');
const $main = document.querySelector('main');

function sendMessage() {
	// Letting all the other browsers know what you typed
	socket.emit('chat', {name, text: $textarea.value});
	
	// Displaying the message into a new div and adding it to the main element
	const div = document.createElement('div');
	div.className = 'me';
	div.innerHTML = `<b>${name}:</b> <span>${$textarea.value}</span>`;
	$main.appendChild(div);
	$textarea.value = '';
	
	// Automatically scroll to the bottom of the message
	$main.scrollTo(0,$main.scrollHeight);
}

// Sending the message when the button is clicked
$button.addEventListener('click', sendMessage);

// Moving the cursor to the textbox so the user can start typing
$textarea.focus();
```

Finally we have to display the message that someone sent to us:
```javascript
socket.on('chatresponse', function(data) {
	const div = document.createElement('div');
	div.className = 'you';
	div.innerHTML = `<b>${data.data.name}:</b> <span>${data.data.text}</span>`;
	$main.appendChild(div);
	$main.scrollTo(0,$main.scrollHeight);
});
```

> **Exercise**:
> - Remove the hard coded chat messages on top
> - Test your chat application
> - To create different rooms just add `?ROOM_NAME` to the end of the url. `ROOM_NAME` is what ever you want to call it.
> - Send images or videos by just entering the `html` for that image or video. For example:
	- `<img src="https://media.tenor.co/images/0872d90502401d2260bf8704ae77a2a9/tenor.gif">` will send a gif of a sleepy minion
	- `<iframe width="560" height="315" src="https://www.youtube.com/embed/5uNujDrsEMQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>` will send a youtube video

***

<h2 id='starterapp'>The final product</h2>

```html
<!DOCTYPE html>
<html>
	<head>
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link href="https://fonts.googleapis.com/css2?family=Inconsolata&family=Fredericka+the+Great&family=Mali&display=swap" rel="stylesheet">
		<title>Private Chat</title>
		<style>
			* {
				box-sizing:border-box;
				margin:0;
				padding:0;
			}
			body {
				display:grid;
				grid-template-rows: 64px auto 100px;
				grid-template-columns: auto 600px auto;
				width:100vw;
				height:100vh;
				overflow: hidden;
				font-family: system-ui, san-serif;
				background-color: #fcd411;
			}
			header {
				grid-column-start: 2;
				grid-column-end: 3;
				text-align:center;
				display:flex;
				align-items:center;
				justify-content:center;
				background-color: #2e2e30;
				color: #fcd411;
			}
			header > h1 {
				font-family: 'Fredericka the Great', cursive;
				font-size: 2em;
			}
			main {
				grid-column-start: 2;
				grid-column-end: 3;
				list-style:none;
				padding: 24px;
				display:flex;
				flex-direction:column;
				align-items:center;
				justify-content:flex-start;	
				background-color: white;
				overflow-y: auto;
				overflow-x: hidden;
			}
			main > div {
				width: 100%;
				font-size: 18px;
				margin: 8px 0;
			}
			main > div.me {
				font-family: 'Mali', cursive;
				text-align: right;
			}
			main > div.you {
				font-family: 'Inconsolata', monospace;
				text-align:left;
			}
			footer {
				grid-column-start: 2;
				grid-column-end: 3;
				display:grid;
				grid-template-columns: auto 80px;
				background-color: #fcd411;
			}
			footer > textarea {
				font-family: 'Mali', cursive;
				font-size: 18px;
				padding: 8px 16px;
				resize: none;
			}
			footer > button {
				font-family: 'Fredericka the Great', cursive;
				font-size: 20px;
				background-color: #fcd411;
			}
			@media only screen and (max-width: 768px) {
				body {
					height: calc(100vh - 114px);
					grid-template-columns: auto 100% auto;
				}
			}
		</style>
		<script src='/libs/socketio.js'></script>
		<script type='module'>
			// GET THE PERSON'S NAME
			
			let name = localStorage.getItem('name');
			if(!name) {
				name = prompt("What is your name?")
				localStorage.setItem('name', name);
			}
			
			
			// REGISTER COMMUNICATIONS
			const socket = io('/tunnel');
			async function initializeSockets() {
				const res = await fetch('/tunnel/register', {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({
						events: ['chat']
					})
				});
				
				const resp = await res.json();
			
				if(resp.error) return alert(resp.error)
				
			
				socket.on('chatresponse', function(data) {
					const div = document.createElement('div');
					div.className = 'you';
					div.innerHTML = `<b>${data.data.name}:</b> <span>${data.data.text}</span>`;
					$main.appendChild(div);
					$main.scrollTo(0,$main.scrollHeight);
				});
				
				socket.on('userconnected', (socketId) => {
					console.log('userconnected: ' + socketId);
				});
				
				socket.on('userdisconnected', (socketId) => {
					console.log('disconnected: ' + socketId);
				})
	
			}
			initializeSockets();
			
			// SENDING CHAT MESSAGE
			const $button = document.querySelector('button');
			const $textarea = document.querySelector('textarea');
			const $main = document.querySelector('main');
			
			function sendMessage() {
				socket.emit('chat', {name, text: $textarea.value});
				
				const div = document.createElement('div');
				div.className = 'me';
				div.innerHTML = `<b>${name}:</b> <span>${$textarea.value}</span>`;
				$main.appendChild(div);
				$textarea.value = '';
				$main.scrollTo(0,$main.scrollHeight);
			}

			$button.addEventListener('click', sendMessage);
			$textarea.focus();
		</script>
	</head>
	<body>
		<header>
			<h1>🔒 Private Chat </h1>
		</header>
		<main>
			<div class='you'>Welcome!</div>
			<div class='me'></div>
		</main>
		<footer>
			<textarea placeholder='Type your message here...'></textarea>
			<button>Send</button>
		</footer>
	</body>
</html>
```

***

<h2 id='listofresources'>List of Resources</h2>

### HTML References
1. HTML Elements:<br> <https://developer.mozilla.org/en-US/docs/Web/HTML/Element>

### CSS References

1. Flex Box:<br> <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Flexible_Box_Layout/Basic_Concepts_of_Flexbox>
2. Grid Layout:<br> <https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Grid_Layout/Basic_Concepts_of_Grid_Layout>

### Javascript References
1. Socket IO<br> <https://socket.io/>

<style>
	img {
		box-shadow:0 10px 16px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
		display:block;
		margin: 1rem auto 3rem;
	}
	
	pre > code {
		font-size: 16px;
		color:lightgreen;
	}
</style>

#!/usr/bin/node
const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
let output = '';

for (let i = 0; i < languages.length; i += 1) {
  output += `${languages[i]}\n`;
}

console.log(output.trim());
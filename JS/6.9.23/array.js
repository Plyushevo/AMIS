let games = ['CS:go', 'Dota2', 'RimWorld', 'Mount&Blade2:Bannerlord']
let length = games.length

console.log(length)
let text = '<ul>'
for (let i = 0; i < length; i++) {
    text += '<li>' + games[i] + '</li>';
}

text += '</ul>'
document.querySelector('.demo').innerHTML = text
document.get
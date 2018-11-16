document.addEventListener('DOMContentLoaded', function(){
  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
  // When connected, config buttons
  socket.on('connect', ()=>{
    document.querySelectorAll('button').forEach(button=>{
      button.onclick = ()=>{
        const selection = button.dataset.vote;
        socket.emit('submit vote', {'selection':selection});
      };
    });
  });
  // When a new vote is announced, add to the list
  socket.on('vote totals', data =>{
    document.querySelector('#yes').innerHTML = data.yes;
    document.querySelector('#no').innerHTML = data.no;
    document.querySelector('#maybe').innerHTML = data.maybe;
  });
});

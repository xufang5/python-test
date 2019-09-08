var btn = document.getElementById("show");
btn.onclick = function(){
  BootstrapDialog.show({
      title: 'Create A Defact',
      message: $('<textarea class="form-control" placeholder="Try to input multiple lines here..."></textarea>'),
      buttons: [{
          label: '(Enter) Button A',
          cssClass: 'btn-primary',
          hotkey: 13, // Enter.
          action: function() {
              alert('You pressed Enter.');
          }
      }]
  });
}

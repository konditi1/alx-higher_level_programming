$('#add_item').click(() => {
    const item = $('<li></li>').text('Item');
    $('.my_list').append(item);
  });
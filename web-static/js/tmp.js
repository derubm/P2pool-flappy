    d3.json('../recent_blocks', function(blocks) {
      var tr = d3.select('#blocks').selectAll().data(blocks).enter().append('tr');
      tr.append('td').text(function(block){return block.number});
      tr.append('td').text(function(block){return new Date(1000*block.ts).toString()});
      tr.append('td').append('a').text(function(block){return block.hash}).attr('href', function(block){return currency_info.block_explorer_url_prefix + block.hash});
      tr.append('td').append('a').text('>').attr('href', function(block){return 'share.html#' + block.share});
    });
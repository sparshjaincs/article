

    //setInterval(function() {
    // your code goes here...
    //save();
//}, 100 * 1000);


   
$(function(){
  
   $(".lined").linedtextarea({
    	
    
    });
})



    function copyToClipboard() {
    var textBox = document.getElementById("shareinput");
    textBox.select();
    document.execCommand("copy");
    document.getElementById('copystatus').innerHTML = '<span class="mt-1 p-0" style="color:#f0ad4e;" ><i class="fa fa-dot-circle-o"></i> Copied</span>';
    $("#copystatus").children().delay(5000).fadeOut(800);
}

<script type="text/javascript">
    function remove()
    {
    
       $("#inp").removeAttr('disabled'); //removes the disabled attribut from the  
                                              //element whose id is 'date_end'
    }


    function savefile(){
        var val = document.getElementById('inp').value;
      
        $.ajax({
            type:'GET',
            url : '/compiler/savefile/{{id}}/',
            data:{
                file_name: val,
            },
            success:function(json){
                json = JSON.parse(json);
                console.log(json);
                document.getElementById('inp').disabled = true;
            },
            error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText);
            }

        });
    }


    function save(){
        $.ajax({
        type:'POST',
        url:'/compiler/save/{{id}}/',
        data:{
            title:$('#title').val(),
            description:$('#textbox').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(json){
            json = JSON.parse(json);
            console.log(json);
            var str = ' <span class="btn btn-sm mr-2 mt-1 btn-outline-warning  rounded-pill" style="border:none;" ><i class="fa fa-dot-circle-o"> '+ json+ '</span>'
            document.getElementById('savestatus').innerHTML = str;
            $("#savestatus").children().delay(5000).fadeOut(800);   
        
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
});
    }


$("select").mouseup(function() {
    var code = document.getElementById('title').value;

    $.ajax({
        type:'GET',
        url:'/compiler/temp/{{id}}/',
        data:{
            lang:code,
        },
        success:function(json){
            json = JSON.parse(json);
            document.getElementById('textbox').innerHTML = json['instance'];
            
        }
    });
});


    function submit(){
        document.getElementById('status').innerHTML = "Output: <span class='badge badge-sm badge-secondary'> Running </span>";
           
        $.ajax({
        type:'POST',
        url:'/compiler/test/',
        data:{
            title:$('#title').val(),
            description:$('#textbox').val(),
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
            action: 'post'
        },
        success:function(json){
            json = JSON.parse(json);
            var node = document.createElement("P");
            
            node.innerHTML ="<p style='color:#449D44;'> Finished in " + json['output'][2] + " ms" + "</p>"+ "<pre>" + json['output'][0] + "</pre><hr>" ;
            document.getElementById("outputconsole").appendChild(node);

            if (json['output'][1] == 0){
                document.getElementById('status').innerHTML = "Output: <span class='badge badge-sm badge-success'> Finished </span>";
            }
            else{
                document.getElementById('status').innerHTML = "Output: <span class='badge badge-sm badge-danger'> Runtime Error </span>";
            }
        
        },
        error : function(xhr,errmsg,err) {
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
    }
});
    }


    function selectTextareaLine(area,line){
        
    }
function getLineNumberAndColumnIndex(textarea){
     var textLines = textarea.value.substr(0, textarea.selectionStart).split("\n");
     var currentLineNumber = textLines.length;
     var currentColumnIndex = textLines[textLines.length-1].length;
    document.getElementById('rowcolumns').innerHTML = "row: "+ currentLineNumber + " column: " + currentColumnIndex;
    
  }

    

    document.getElementById('textbox').addEventListener('keydown', function(e) {
  if (e.key == 'Tab') {
    e.preventDefault();
    var start = this.selectionStart;
    var end = this.selectionEnd;

    // set textarea value to: text before caret + tab + text after caret
    this.value = this.value.substring(0, start) +
      "\t" + this.value.substring(end);

    // put caret at right position again
    this.selectionStart =
      this.selectionEnd = start + 1;
  }
});



  
    /**
 * http://jsfiddle.net/rudiedirkx/WwCe3/
 *
 * To do:
 * - tab/shift tab: (un)indent a line on command
 * - 'mass tab': select several lines and (un)indent them all (requires TAB)
 * - support for undo/redo, by using `execCommand('insertText')`
 */

function doAutoIndent(ta, indent) {
    indent || (indent = "\t");
    
    function setValue(text) {
        ta.value = text;
        return ta.value;
    }
    
    function str_repeat(str, n) {
        var out = '';
        while (n--) out += str;
        return out;
    }
    
    function isIndented(line) {
        var regex = new RegExp('^(' + indent + '+)', 'g'),
            match = line.match(regex);
        return match && match[0].length / indent.length || 0;
    }
    
    function addIndent(before, after, num) {
        // num = num ? ~~num : 1;
        if ( !num ) return;
        ta._lastValue = setValue(before + str_repeat(indent, num) + after);
        ta.selectionStart = ta.selectionEnd = before.length + indent.length * num;
    }
    
    function removeIndent(before, after) {
        var remove = before.slice(before.length - 1 - indent.length, before.length - 1);
        if ( remove != indent ) {
            return;
        }
        
        ta._lastValue = setValue(before.slice(0, -1-indent.length) + '}' + after);
        ta.selectionStart = ta.selectionEnd = before.length - indent.length;
    }
    
    function getPrevLine(before) {
        var lines = ta.value.split(/\n/g),
            line = before.trimRight().split(/\n/g).length - 1;
        return lines[line] || '';
    }
    
    function onKeyUp(e) {
        var lastValue = ta._lastValue === undefined ? ta.defaultValue : ta._lastValue,
            change = ta.value.length - lastValue.length;
        ta._lastValue = ta.value;
        if ( !change ) {
            return;
        }
        
        var caret = ta.selectionStart,
            added = change > 0 && ta.value.substr(caret - change, change) || '',
            removed = change < 0 && lastValue.substr(caret, -change) || '';
        
        var code = e.keyCode;
        var value = ta.value,
            before = value.substr(0, caret),
            after = value.substr(caret),
            lastChar = before.trim().slice(-1),
            nextChar = after.substr(0, 1);
        
        // ENTER
        if ( code == 13 ) {
            
            // Immediately after a {
            if ( lastChar == '{' ) {
                var prevLine = getPrevLine(before),
                    indents = isIndented(prevLine),
                    more = nextChar == '}' ? 0 : 1;
                return addIndent(before, after, indents + more);
            }
            if ( lastChar == ':' ) {
                var prevLine = getPrevLine(before),
                    indents = isIndented(prevLine),
                    more = nextChar == '}' ? 0 : 1;
                return addIndent(before, after, indents + more);
            }
            
            // After an indented line
            var prevLine = getPrevLine(before),
                indents = isIndented(prevLine),
                more = nextChar == '}' ? -1 : 0;
            if ( indents + more > 0 ) {
                addIndent(before, after, indents + more);
            }
        }
        else if ( added == '}' ) {
            removeIndent(before, after);
        }
    }
    
    ta.addEventListener('keyup', onKeyUp, false);
}

var tas = document.querySelectorAll('textarea');
[].forEach.call(tas, function(ta) {
    doAutoIndent(ta, "\t");
});




    
(function($) {

	$.fn.linedtextarea = function(options) {
		
		// Get the Options
		var opts = $.extend({}, $.fn.linedtextarea.defaults, options);
		
		
		/*
		 * Helper function to make sure the line numbers are always
		 * kept up to the current system
		 */
		var fillOutLines = function(codeLines, h, lineNo){
			while ( (codeLines.height() - h ) <= 0 ){
				if ( lineNo == opts.selectedLine )
					codeLines.append("<div class='lineno lineselect'>" + lineNo + "</div>");
				else
					codeLines.append("<div class='lineno'>" + lineNo + "</div>");
				
				lineNo++;
			}
			return lineNo;
		};
		
		
		/*
		 * Iterate through each of the elements are to be applied to
		 */
		return this.each(function() {
			var lineNo = 1;
			var textarea = $(this);
			
			/* Turn off the wrapping of as we don't want to screw up the line numbers */
			textarea.attr("wrap", "off");
			textarea.css({resize:'none'});
			var originalTextAreaWidth	= textarea.outerWidth();

			/* Wrap the text area in the elements we need */
			textarea.wrap("<div class='linedtextarea'></div>");
			var linedTextAreaDiv	= textarea.parent().wrap("<div class='linedwrap' style='width:" + originalTextAreaWidth + "px'></div>");
			var linedWrapDiv 			= linedTextAreaDiv.parent();
			
			linedWrapDiv.prepend("<div class='lines' style='width:50px'></div>");
			
			var linesDiv	= linedWrapDiv.find(".lines");
			linesDiv.height( textarea.height() + 6 );
			
			
			/* Draw the number bar; filling it out where necessary */
			linesDiv.append( "<div class='codelines'></div>" );
			var codeLinesDiv	= linesDiv.find(".codelines");
			lineNo = fillOutLines( codeLinesDiv, linesDiv.height(), 1 );

			/* Move the textarea to the selected line */ 
			if ( opts.selectedLine != -1 && !isNaN(opts.selectedLine) ){
				var fontSize = parseInt( textarea.height() / (lineNo-2) );
				var position = parseInt( fontSize * opts.selectedLine ) - (textarea.height()/2);
				textarea[0].scrollTop = position;
			}

			
			/* Set the width */
			var sidebarWidth					= linesDiv.outerWidth();
			var paddingHorizontal 		= parseInt( linedWrapDiv.css("border-left-width") ) + parseInt( linedWrapDiv.css("border-right-width") ) + parseInt( linedWrapDiv.css("padding-left") ) + parseInt( linedWrapDiv.css("padding-right") );
			var linedWrapDivNewWidth 	= originalTextAreaWidth - paddingHorizontal;
			var textareaNewWidth			= originalTextAreaWidth - sidebarWidth - paddingHorizontal - 20;

			textarea.width( textareaNewWidth );
			linedWrapDiv.width( linedWrapDivNewWidth );
			

			
			/* React to the scroll event */
			textarea.scroll( function(tn){
				var domTextArea		= $(this)[0];
				var scrollTop 		= domTextArea.scrollTop;
				var clientHeight 	= domTextArea.clientHeight;
				codeLinesDiv.css( {'margin-top': (-1*scrollTop) + "px"} );
				lineNo = fillOutLines( codeLinesDiv, scrollTop + clientHeight, lineNo );
			});


			/* Should the textarea get resized outside of our control */
			textarea.resize( function(tn){
				var domTextArea	= $(this)[0];
				linesDiv.height( domTextArea.clientHeight + 6 );
			});

		});
	};

  // default options
  $.fn.linedtextarea.defaults = {
  	selectedLine: -1,
  	selectedClass: 'lineselect'
  };
})(jQuery);

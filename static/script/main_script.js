var Username = ""
const URL = "https://sheet-cheat-api.herokuapp.com/"

var options = [letter_color, letter_size, letter_distance, letter_gap, paper_type, has_holes, paper_color, paper_size, line_color, square_dimension]
var selected_options = []

var selected_style = null

function generate(){
    document.getElementById("output_section").style.display = "flex"
}

function onOptionChange(){
    for(let o=0; o<options.length; o++){
        selected_options[o] = options[o].getSelectedValue()
    }
    console.log(selected_options)
}

$(document).ready(function(){
    selected_options = [letter_color.getSelectedValue(), letter_size.getSelectedValue(), letter_distance.getSelectedValue(), letter_gap.getSelectedValue(), paper_type.getSelectedValue(), has_holes.getSelectedValue(), paper_color.getSelectedValue(), paper_size.getSelectedValue(), line_color.getSelectedValue(), square_dimension.getSelectedValue()]
    changeLoginStatus()
})




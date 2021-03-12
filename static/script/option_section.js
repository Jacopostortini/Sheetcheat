class Option{
    constructor(id_array, default_id, default_value, add_option_id, new_input_id){
        this.id_array = id_array
        this.default_id = default_id
        this.default_value = default_value
        this.add_option_id = add_option_id
        this.new_input_id = new_input_id
        this.selected_id = "";
    }

    selectObject(id) {
        this.dehighlightAll()
        this.highlightObject(id)
        this.selected_id = id
        onOptionChange()
    }

    dehighlightAll() {
        for(let id of this.id_array){
            document.getElementById(id).style.borderColor = "lightgray"
            document.getElementById(id).style.borderWidth = "1px"
        }
    }

    highlightObject(id){
        document.getElementById(id).style.borderColor = "black"
        document.getElementById(id).style.borderWidth = "2px"
    }

    increase(){
        var current = document.getElementById(this.new_input_id).innerHTML
        if(current != "+"){
            document.getElementById(this.new_input_id).innerHTML = Number(current)+1
        }
    }

    decrease(){
        var current = document.getElementById(this.new_input_id).innerHTML
        if(current != "+" && Number(current)>0){
            document.getElementById(this.new_input_id).innerHTML = Number(current)-1
        }
    }

    resetNewInput(){
        if(this.new_input_id!=null){
            if(String(this.new_input_id).includes("picker")){
                document.getElementById(this.add_option_id).style.backgroundColor = "white"
            } else{
                document.getElementById(this.new_input_id).innerHTML = "+"
            }
        }
    }

    getSelectedValue(){
        switch(this.selected_id){
            case "plain_paper_type_box":
                return 0
            case "squares_paper_type_box":
                return 1
            case "lines_paper_type_box":
                return 2
            case "has_holes_box":
                return true
            case "has_not_holes_box":
                return false
            default:
                return this.default_value;
        }
    }
}

class LetterColorOption extends Option{
    selectObject(id){
        super.selectObject(id)
        if(id==this.add_option_id){
            var new_c = document.getElementById(this.new_input_id)
            document.getElementById(id).style.backgroundColor = new_c.value
        }
    }

    getSelectedValue(){
        switch(this.selected_id){
            case "red_letter_color_box":
                return "red"
            case "black_letter_color_box":
                return "black"
            case "blue_letter_color_box":
                return "blue"
            case "add_letter_color_box":
                return document.getElementById(this.new_input_id).value
            default:
                return this.default_value;
        }
    }
}

class LetterSizeOption extends Option{
    selectObject(id){
        super.selectObject(id)
        if(id==this.add_option_id){
            var current = document.getElementById(this.new_input_id)
            if(current.innerHTML=="+"){
                document.getElementById(this.new_input_id).innerHTML = this.default_value
                document.getElementById("up_letter_size").style.visibility = "visible"
                document.getElementById("down_letter_size").style.visibility = "visible"
            }
        }
    }

    getSelectedValue(){
        switch(this.selected_id){
            case "3_letter_size_box":
                return 3
            case "4_letter_size_box":
                return 4
            case "5_letter_size_box":
                return 5
            case "add_letter_size_box":
                return Number(document.getElementById(this.new_input_id).innerHTML)
            default:
                return this.default_value;
        }
    }
    
}

class LetterDistanceOption extends Option{
    selectObject(id){
        super.selectObject(id)
        if(id==this.add_option_id){
            var current = document.getElementById(this.new_input_id)
            if(current.innerHTML=="+"){
                document.getElementById(this.new_input_id).innerHTML = this.default_value
                document.getElementById("up_letter_distance").style.visibility = "visible"
                document.getElementById("down_letter_distance").style.visibility = "visible"
            }
        }
    }

    getSelectedValue(){
        switch(this.selected_id){
            case "1_letter_distance_box":
                return 1
            case "2_letter_distance_box":
                return 2
            case "3_letter_distance_box":
                return 3
            case "add_letter_distance_box":
                return Number(document.getElementById(this.new_input_id).innerHTML)
            default:
                return this.default_value;
        }
    }
}

class LetterGapOption extends Option{
    selectObject(id){
        super.selectObject(id)
        if(id==this.add_option_id){
            var current = document.getElementById(this.new_input_id)
            if(current.innerHTML=="+"){
                document.getElementById(this.new_input_id).innerHTML = this.default_value
                document.getElementById("up_letter_gap").style.visibility = "visible"
                document.getElementById("down_letter_gap").style.visibility = "visible"
            }
        }
    }

    getSelectedValue(){
        switch(this.selected_id){
            case "0_letter_gap_box":
                return 0
            case "1_letter_gap_box":
                return 1
            case "2_letter_gap_box":
                return 2
            case "add_letter_gap_box":
                return Number(document.getElementById(this.new_input_id).innerHTML)
            default:
                return this.default_value;
        }
    }
}

class PaperColorOption extends Option{
    selectObject(id){
        super.selectObject(id)
        if(id==this.add_option_id){
            var new_c = document.getElementById(this.new_input_id)
            document.getElementById(id).style.backgroundColor = new_c.value
        }
    }

    getSelectedValue(){
        switch(this.selected_id){
            case "white_paper_color_box":
                return "white"
            case "add_paper_color_box":
                return document.getElementById(this.new_input_id).value
            default:
                return this.default_value;
        }
    }
    
}

class PaperSizeOption extends Option{
    selectObject(id){
        //onOptionChange()
        if(id == "default"){
            document.getElementById(this.id_array[0]).value = this.default_value[0]
            document.getElementById(this.id_array[1]).value = this.default_value[1]
        }
    }

    dehighlightAll(){
        document.getElementById(this.id_array[0]).value = ""
        document.getElementById(this.id_array[1]).value = ""
    }

    getSelectedValue(){
        return [document.getElementById(this.id_array[0]).value, document.getElementById(this.id_array[1]).value]
    }
}

class LineColorOption extends Option{
    selectObject(id){
        super.selectObject(id)
        if(id==this.add_option_id){
            var new_c = document.getElementById(this.new_input_id)
            document.getElementById(id).style.backgroundColor = new_c.value
        }
    }

    getSelectedValue(){
        switch(this.selected_id){
            case "blue_line_color_box":
                return "blue"
            case "black_line_color_box":
                return "black"
            case "add_line_color_box":
                return document.getElementById(this.new_input_id).value
            default:
                return this.default_value;
        }
    }
}

class SquareDimensionOption extends Option{
    selectObject(id){
        super.selectObject(id)
        if(id==this.add_option_id){
            var current = document.getElementById(this.new_input_id)
            if(current.innerHTML=="+"){
                document.getElementById(this.new_input_id).innerHTML = this.default_value
                document.getElementById("up_square_dimension").style.visibility = "visible"
                document.getElementById("down_square_dimension").style.visibility = "visible"
            }
        }
    }

    getSelectedValue(){
        switch(this.selected_id){
            case "4_square_dimension_box":
                return 4
            case "5_square_dimension_box":
                return 5
            case "add_square_dimension_box":
                return Number(document.getElementById(this.new_input_id).innerHTML)
            default:
                return this.default_value;
        }
    }
}

//ATTRIBUTES DECLARATION
var letter_color = new LetterColorOption(["red_letter_color_box", "black_letter_color_box", "blue_letter_color_box", "add_letter_color_box"],"black_letter_color_box", "black", "add_letter_color_box", "new_letter_color_picker")

var letter_size = new LetterSizeOption(["3_letter_size_box", "4_letter_size_box", "5_letter_size_box", "add_letter_size_box"],"4_letter_size_box", 4, "add_letter_size_box", "new_letter_size")

var letter_distance = new LetterDistanceOption(["1_letter_distance_box", "2_letter_distance_box", "3_letter_distance_box", "add_letter_distance_box"],"1_letter_distance_box", 1, "add_letter_distance_box", "new_letter_distance")

var letter_gap = new LetterGapOption(["0_letter_gap_box", "1_letter_gap_box", "2_letter_gap_box", "add_letter_gap_box"],"0_letter_gap_box", 0, "add_letter_gap_box", "new_letter_gap")

var paper_type = new Option(["plain_paper_type_box", "squares_paper_type_box", "lines_paper_type_box"],"squares_paper_type_box", 1, null, null)

var has_holes = new Option(["has_holes_box", "has_not_holes_box"], "has_holes_box", true, null, null)

var paper_color = new PaperColorOption(["white_paper_color_box", "add_paper_color_box"],"white_paper_color_box", "white", "add_paper_color_box", "new_paper_color_picker")

var paper_size = new PaperSizeOption(["paper_width_input_box", "paper_height_input_box"], "default", [210, 297], null, null)

var line_color = new LineColorOption(["blue_line_color_box", "black_line_color_box", "add_line_color_box"],"black_line_color_box", "black", "add_line_color_box", "new_line_color_picker")

var square_dimension = new SquareDimensionOption(["4_square_dimension_box", "5_square_dimension_box", "add_square_dimension_box"],"4_square_dimension_box", 4, "add_square_dimension_box", "new_square_dimension")


//ATTRIBUTES BUTTONS
function eraseOptions(){
    for(let option of options){
        option.dehighlightAll()
        option.resetNewInput()
    }
    for(let arrow of document.getElementsByClassName("arrow_up")){
        arrow.style.visibility = "hidden"
    }
    for(let arrow of document.getElementsByClassName("arrow_down")){
        arrow.style.visibility = "hidden"
    }

    document.getElementById("output_section").style.display = "none"
}

function defaultOptions(){
    for(let option of options){
        option.selectObject(option.default_id)
    }
}
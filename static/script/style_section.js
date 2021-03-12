class DefaultStyle{
    constructor(id_array){
        this.id_array = id_array
    }
    
    selectObject(id){
        this.dehighlightAll()
        document.getElementById(id).style.borderColor = "black"
        document.getElementById(id).style.borderWidth = "2px"
        selected_style = this.id_array.indexOf(id)
    }
    
    dehighlightAll(){
        for(let id of this.id_array){
            document.getElementById(id).style.borderColor = "lightgray"
            document.getElementById(id).style.borderWidth = "1px"
        }
    }
    
}

//STYLE PICKER DECLARATION
var style_picker = new DefaultStyle(["style_image_container1", "style_image_container2", "style_image_container3", "style_image_container4"])

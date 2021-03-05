var sum = 0
var randnum = 1000;

var changesum = function(type, num) {
    if(type == "add"){
        sum += num;
    } else {
        sum -= num;
    }
    console.log(sum);
    if(sum == randnum){
        $("#get-random").css("background-color", "gold");
    }
}
$(document).ready(function() {
    $("#get-random").click(function() {
        randnum = Math.random()*100 | 0;
        $("#get-random").text(randnum);
        $("#get-random").css("background-color", "rgba(66,133,244, .5)");
        $("#digits div").text("0");
        sum = 0;
    })
    $("#one").click(function(){
        if($("#one").text() == "0"){
            $("#one").text("1")
            changesum("add", 128);
        } else {
            $("#one").text("0")
            changesum("fd", 128);
        }
    })
    $("#two").click(function(){
        if($("#two").text() == "0"){
            $("#two").text("1")
            changesum("add", 64);
        } else {
            $("#two").text("0")
            changesum("fd", 64);
        }
    })
    $("#three").click(function(){
        if($("#three").text() == "0"){
            $("#three").text("1")
            changesum("add", 32);
        } else {
            $("#three").text("0")
            changesum("fd", 32);
        }
    })
    $("#four").click(function(){
        if($("#four").text() == "0"){
            $("#four").text("1")
            changesum("add", 16);
        } else {
            $("#four").text("0")
            changesum("fd", 16);
        }
    })
    $("#five").click(function(){
        if($("#five").text() == "0"){
            $("#five").text("1")
            changesum("add", 8);
        } else {
            $("#five").text("0")
            changesum("fd", 8);
        }
    })
    $("#six").click(function(){
        if($("#six").text() == "0"){
            $("#six").text("1")
            changesum("add", 4);
        } else {
            $("#six").text("0")
            changesum("fd", 4);
        }
    })
    $("#seven").click(function(){
        if($("#seven").text() == "0"){
            $("#seven").text("1")
            changesum("add", 2);
        } else {
            $("#seven").text("0")
            changesum("fd", 2);
        }
    })
    $("#eight").click(function(){
        if($("#eight").text() == "0"){
            $("#eight").text("1")
            changesum("add", 1);
        } else {
            $("#eight").text("0")
            changesum("fd", 1);
        }
    })
})

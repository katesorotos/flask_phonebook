$("#business_name").hide();

function remove_name_input(that) {
   $("#business_type").show();
    $("#business_name").hide();
}


$("#type").click(function(event) {
  remove_name_input(this);
});

function remove_type_input(that) {
   $("#business_name").show();
    $("#business_type").hide();
}


$("#name").click(function(event) {
  remove_type_input(this);
});

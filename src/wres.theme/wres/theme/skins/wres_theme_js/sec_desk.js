
function hideOrShowDoctorVisits(){
    /* this function is called for each option.
    If the option is the selected one, The function
    fadeIn all trs (visits) of the doctor, else,
    the function hide all trs (visits) of the doctor.
    Using "slow" effect here causes unpredictable
    behaviors, since this effect has a considerable
    delay, and the element will be in a state that was
    not expected by the hideTableOrNot steps.
    */
	var doctor_id = this.value;
    //if selected, show (fadeIn), else hide.
	if (this.selected == true) {
		var selector = "tr." + doctor_id;
		$(selector).show();
	}
	else {
		if(doctor_id != '') {
			var selector = "tr." + doctor_id;
			$(selector).hide();
		}
	}
}

function hideTableOrNotStep1() {
    /*the table need to be visible, so hideOrShowDoctorVisits
    can show trs of the selected doctor.
    */
    $(".visits_table").show();
    $(".visits-message").show();
    $(".not-for-this-doctor").hide();
}

function hideTableOrNotStep2() {
    /* hide table if there is not any visit being
    showed.
    */
    if ($(".visit:visible").length == 0) {
        $(".visits_table").hide("slow");
        $(".visits-message").hide("slow");
        /* avoid duplication of "non exists" message */
        if($("#no-visits:visible").length == 0) {
            $(".not-for-this-doctor").show("slow");
        }
    }
    else {
        $(".visits_table").show("slow");
    }
}

function reloadVisitsOnScreen() {
    /* Show or hide doctors visits depending on
    which doctor is selected.
    if 'Todos os medicos' selected, show all trs
    else: pass throw all options and leave showing
    only the selected one.
    */
    hideTableOrNotStep1();
    if($("option:selected").get(0).value == "") {
        $("tr").show();
    }
    else {
        $("option").each(hideOrShowDoctorVisits);
    }
    hideTableOrNotStep2();
}

function loadPatientTip(index){

     var patient_url = $("#patient_url"+index).val()
     var AmIDoctor = $("#AmIDoctor").val()
     if (AmIDoctor == 1){
        $("#patient_link"+index).qtip({
            content: "<a href='"+patient_url+"'>Dados</a><br><a href='"+patient_url+"/chartFolder"+"'>Prontuário</a>",
            position:{
                corner: "rigthMiddle",
                adjust:
                    {
                        x: 100,
                        y: 0
                    }

            },
            style: {
                padding: 2,
                background: '#DDDDDD',
                color: 'black',
                textAlign: 'center',
                fontSize: 13,
                border: {
                    radius: 2
                }
            },
            show: 'click',
            hide: {
                fixed: true,
                when: {
                    event: 'unfocus'
                }
            }

            })
        }
    else {
        $("#patient_link"+index).qtip({
            content: "<a href='"+patient_url+"'>Dados</a>",
            position:{
                corner: "rigthMiddle",
                adjust:
                    {
                        x: 100,
                        y: 0
                    }

            },
            style: {
                padding: 2,
                background: '#DDDDDD',
                color: 'black',
                textAlign: 'center',
                fontSize: 13,
                border: {
                    radius: 2
                }
            },
            show: 'click',
            hide: {
                fixed: true,
                when: {
                    event: 'unfocus'
                }
            }

            })
        }

    }

$(document).ready(function(){
	var show_visits_reloaded = false;
        /*var fez_requisicao = false;*/

	$("#doctor_select").change(function(){
	   reloadVisitsOnScreen();
	})


	$(".show_visits").delegate("a.change_state_link", "click", function(event) {
        event.preventDefault();

        /* esconde links e mostra loader gif */
        pai = $(this).parent();
        avo = pai.parent();
        avo.children("img").show();
        pai.hide();

        href = $(this).attr('href');
        $.post(href, function(data) {
        	  if ($("#show_today_visits").is(":visible")) {
        		  $("#show_today_visits").load(location.href + " #show_today_visits");
        	  }
        	  else {
        		  $("#show_tomorrow_visits").load(location.href + " #show_tomorrow_visits");
        	  }
        })
	})

	$('.show_visits').ajaxComplete(function(e, xhr, settings) {
        /* this avoid reloadVisitsOnScreen to be executed in Doctor sec_desk, since
        the doctor already see only his visits. */
        if($("option:selected").length > 0) {
            reloadVisitsOnScreen();
        }
	})

});

function patientClick(){

	var data = {};
	var url = document.getElementById("patient_url").value;
	var extra = '/SFLight_patient_view';
	var titulo = 'Detalhes do Paciente';
	$dialog_content = $('#dialog_content');
	$dialog_content.empty();
	$dialog_content.dialog( "destroy" );
	$.get(url+extra, data,
	      function (msg) {
	          $dialog_content.append(msg);
	          $dialog_content.dialog({
	            width: 'auto',
	            autoOpen: true,
	            modal: true,
	            title: titulo,
	          });
	     }
	);

}

function timeClick(){
	var data = {};
	var url = document.getElementById("visit_url").value;
	var extra = '/SFLight_visit_view';
	var titulo = 'Detalhes da Consulta';
	$dialog_content = $('#dialog_content');
	$dialog_content.empty();
	$dialog_content.dialog( "destroy" );
	$.get(url+extra, data,
	      function (msg) {
	          $dialog_content.append(msg);
	          $dialog_content.dialog({
	            width: 'auto',
	            autoOpen: true,
	            modal: true,
	            title: titulo,
	          });
	     }
	);
}

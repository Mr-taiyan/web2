$(function () {
    var error_email = false;
    var error_pwd = false;
    var error_check_pwd = false;
    var error_name = false;

    $('#email').blur(function () {
    	check_email();
    });

	$('#pwd').blur(function () {
		check_pwd()
    });

	$('#cpwd').blur(function () {
		check_cpwd()
    });

	$('#name').blur(function () {
		check_name();
    });

	$('form[name=form]').submit(function (e) {
		if(error_name == false && error_pwd == false && error_check_pwd == false && error_email == false){
			return true;
		}else{
            alert('fail');
			return false;
		}
    })

    function check_email(){
		var re = /^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$/;

		if(re.test($('#email').val()))
		{
			$.get('/sign_up_exist/?email='+$('#email').val(),function (data) {
				// alert(data.count);
				if(data.count>=1){
					$('#email').next().html('this email has been registered');
					$('#email').next().show();
					error_email = true;
				}else{
					$('#email').next().hide();
					error_email = false;
				}
            })

		}else{
			$('#email').next().html('你输入的邮箱格式不正确');
			$('#email').next().show();
			error_email = true;
		}


	}

	function check_pwd(){
		var len = $('#pwd').val().length;
		if(len<8||len>30)
		{
			$('#pwd').next().html('密码最少8位，最长30位');
			$('#pwd').next().show();
			error_pwd = true;
		}
		else
		{
			$('#pwd').next().hide();
			error_pwd = false;
		}
	}


	function check_cpwd(){
		var pass = $('#pwd').val();
		var cpass = $('#cpwd').val();

		if(pass!=cpass)
		{
			$('#cpwd').next().html('两次输入的密码不一致');
			$('#cpwd').next().show();
			error_check_pwd = true;
		}
		else
		{
			$('#cpwd').next().hide();
			error_check_pwd = false;
		}

	}

	function check_name() {
		var len = $('#name').val().length;
		if(len==0){
			$('#name').next().html('please input your name');
			$('#name').next().show();
		}else if(len>30){
			$('#name').next().html('your name is too long');
			$('#name').next().show();
		}else {
			$('#name').next().hide();
			error_name = false;
		}


    }

});



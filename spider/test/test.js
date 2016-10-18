/**
 * Created by haoxiaotian on 16-10-18.
 */



	var t = 10;
	var file_url= 'http://d23.fmdisk.com/dl.php?Zjc2YzF3MnNrWTVYcmlBaWZVcEllMGNHdWYxRjRjZGlvcHVPRHFvb2ZPR0JmWkk4VDc0OEJIYWlCc0IxWTcvVmxuZCtOS0UvTEZkT2xobmkxRVU0SlZYTDNqMUJ1RWlDc3JkdkdLa2Vyc1A1T09Ib2xSUEtvaWV6U1BhWWl6bGRHQkNJOW5PWkJFaVEyaXJjazVCNlhqcUJoWDR6VFdVUGNaTjlkaVNQOHMxZmpEcFhvK0JTbkE2aEtmbkpxeXJTaU5RZUt0bU9keTZTaUd1NUVzRGY2ZExEZnJZQjRnM1FZOHVrZW5GV1VzQ21TNGFQ';
	function load_down(){
		document.getElementById("seconds").innerHTML=t;
		t = t - 1;
		if(t<=0){
			document.getElementById("d_txt").innerHTML="";
			load_down_addr2('646458');
		}else{
			setTimeout("load_down()",1000);
		}
		/*if(t<=0){
			down();
		}else{
			t = t - 1;
			if( t == 5){
				load_down_addr2('646458');
			}
			setTimeout("load_down()",1000);
		}*/
	}
	/*function down(){
		location = file_url;
		down_process2('646458');
	}*/
	load_down();


function down_process2(file_id){
var e=event||window.event;var ms=e.clientX+"*"+e.clientY;
	$.ajax({
		type : 'post',
		url : 'ajax.php',
		data : 'action=pc_2016101813&file_id='+646458+'&ms='+ms+'&sc='+screen.width+'*'+screen.height,
		dataType : 'text',
		success:function(msg){
			if(msg == 'true'){

			}else{
				alert(msg);
			}
		},
		error:function(){
		}

	});
}
        //ajax.php?action=save_as&file_id=646458&t=0.9184879423596415
        //ajax.php?action=pc_2016101813&file_id=646458&ms=20*30&sc=1366*768
		function save_as(file_id){
	$.ajax({
		type : 'get',
		url : 'ajax.php',
		data : 'action=save_as&file_id='+646458+'&t=0.9184879423596415'+Math.random(),
		dataType : 'text',
		success:function(msg){
			if(msg == 'true'){
				ctsuccess("另存文件操作成功。");
			}else if(msg =='ufile'){
				cterror("此文件已在您的网盘中，不需另存。");
			}else{
				cterror("另存文件操作失败，请重试。");
			}
		},
		error:function(){
		}

	});
}
function favorite_as(user_id){
	$.ajax({
		type : 'post',
		url : 'yythems_ajax.php',
		data : 'action=favorite&uid='+user_id+'&task=to_favorite&t='+Math.random(),
		dataType : 'text',
		success:function(msg){
			if(msg == 'ok'){
				ctsuccess("关注成功");
			}else{
				cterror(msg);
			}
		},
		error:function(){

		}

	});
}

			save_alert = function(){
				cterror("此功能需要登录后才能使用。");
			}
			save_vip = function(){
				cterror("本功能仅对VIP用户开放");
				window.location.href="/vip.php";
			}
			favorite_alert = function(){
				cterror("登录后才能关注");
			}
			down_del_alert = function(){
				cterror("文件已经被删除");
			}

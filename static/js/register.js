function bindCaptchaBtnClick(){
    // 自动寻找相同名称的元素, on 当出现什么操作是执行什么函数
    $("#captcha-btn").on("click", function (event){
        var $this = $(this);
        var email = $("input[name='email']").val();       // 获取input标签 .val()获取值
        // 进行判断
        if(!email){
            alert("请先输入邮箱!");   // 弹出框
            return;
        }
        // ajax 通过js发送网络请求
        $.ajax({
            url: "/user/captcha",
            method: "POST",     // POST请求
            data: {
                "email": email
            },
            // 如果请求成功则返回数据
            success: function (res){
                var code = res['code'];
                if(code == 200){    // 判断是否相等
                    // 取消点击事件
                    $this.off("click");
                    // 开始倒计时
                    var countdown = 60;
                    var timer = setInterval(function (){
                        countdown -= 1;
                        if(countdown > 0){
                            $this.text(countdown + "秒后重新发送");
                        }else{
                            $this.text("获取验证码");
                            // 重新绑定点击事件
                            bindCaptchaBtnClick();
                            // 清除倒计时
                            clearInterval(timer);
                        }
                    }, 1000);    // 一次1000毫秒
                    alert("验证码发送成功, 请前往邮箱查看!");
                }else{  // 如果未成功则返回message信息
                    alert(res['message']);
                }
            }
        })
    });
}


// 等待网页所有元素加载完成后再执行操作
$(function () {
    bindCaptchaBtnClick();
});
function bindBulletframeClick() {
    $('#Bullet_frame1').click(function () {
        $('.toast').toast('show');
    });
}

// 等待网页所有元素加载完成后再执行操作
$(function () {
    bindBulletframeClick();
});
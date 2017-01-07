$(function(){
    var mySwiper01 = new Swiper ('.swiper-container01', {
        slidesPerView : 5,
        speed:300,
        paginationClickable: true,
        spaceBetween: 30,
        slideToClickedSlide:true,
        nextButton: '.arrow-l-big',
        prevButton: '.arrow-r-big',
    });
    var mySwiper02 = new Swiper ('.swiper-container02', {
        nextButton: '.arrow-l-small',
        prevButton: '.arrow-r-small',
    });
    var flags = 0;
    var caseFn = {
        init:function(){
            this.slide();
            this.btnEvent();
        },
        slide:function(){
            var item = $(".swiper-container01");
            item.on("click","li",function(){
                var _this = $(this);
                var liNum = _this.index();
                _this.addClass("swiper-slide-active");
                _this.siblings().removeClass("swiper-slide-active");
                var intro = $('.swiper-slide-active span').text()
                intro = '云途VDP全网发行客户内容累计播放&阅读量已超过20,000,000人/次'
                console.log(intro)
                $('.dbox p').text(intro)
                _this.siblings().removeClass("swiper-slide-next");
                _this.siblings().removeClass("swiper-slide-prev");
                _this.prev().addClass("swiper-slide-prev");
                _this.next().addClass("swiper-slide-next");
                flags = liNum;
                caseFn.cpInfo();
            });         
        },
        btnEvent:function(){
            var item = $(".arrow-l-big,.arrow-r-big");
            item.click(function(){
                var obj = $(".swiper-container01 .swiper-slide-active");
                flags = obj.index()
                caseFn.cpInfo();
            })
        },
        cpInfo:function(){
            var infoObj = $(".cp-introduce .dbox");
            infoObj.eq(flags).removeClass("vdp-hide").siblings().addClass("vdp-hide");
        }
    };
    caseFn.init();     
})
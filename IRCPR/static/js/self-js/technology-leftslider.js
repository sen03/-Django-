$(function(){
    $(document).on("click", ".technologyMenu li", function(){
        var sId = $(this).data("id");  //获取data-id的值
        window.location.hash = sId;  //设置锚点
        loadInner(sId);
    });
    function loadInner(sId){
        var sId = window.location.hash;
        var pathn, i;
        switch(sId){
            case "#technology-robot":  console.log(123);pathn = "technology-robot.html"; i = 0; break;
　　　　　　case "#natural-language": pathn = "technology1.html"; i = 1; break;
            case "#speech-recognition": pathn = "technology1.html"; i = 2; break;
            case "#self-navigation": pathn = "technology-navigation.html"; i = 3; break;
　　　　　　default: pathn = "technology-column.html"; i = 0; break;
        }
        $("#content").load(pathn); //加载相对应的内容
        $(".technologyMenu li").eq(i).addClass("current").siblings().removeClass("current"); //当前列表高亮
    }
    var sId = window.location.hash;
    loadInner(sId);
});

$(function(){
    $(".technologyMenudd").on("click", "dd", function(){
        var sId = $(this).data("id");  //获取data-id的值
        window.location.hash = sId;  //设置锚点
        loadInner(sId);
    });
    function loadInner(sId){
        var sId = window.location.hash;
        var pathn, i;
        switch(sId){
            case "#technology-robot": pathn = "technology-robot.html"; i = 0; break;
　　　　　　case "#natural-language": pathn = "technology1.html"; i = 1; break;
            case "#speech-recognition": pathn = "user_trade.html"; i = 2; break;
            case "#info": pathn = "user_info.html"; i = 3; break;
　　　　　　default: pathn = "technology-column.html"; i = 0; break;
        }
        $("#content").load(pathn); //加载相对应的内容
        $(".technologyMenu li").eq(i).addClass("current").siblings().removeClass("current"); //当前列表高亮
    }
    var sId = window.location.hash;
    loadInner(sId);
});
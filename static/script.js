const input = document.getElementById("school");
const box = document.getElementById("suggestions");


// =======================
// 自动搜索提示
// =======================

if(input){

    input.addEventListener("input", async function () {

        const text = input.value.trim();


        if (text === "") {

            box.innerHTML = "";

            return;

        }



        const response = await fetch("/suggest?q=" + text);

        const data = await response.json();



        box.innerHTML = "";



        data.forEach(function (school) {


            const div = document.createElement("div");


            div.innerText = school;



            div.onclick = function () {

                input.value = school;

                box.innerHTML = "";

            };



            box.appendChild(div);


        });


    });

}





// =======================
// 收藏学校（最多20所）
// =======================


function addFavorite(name){


    let favorites = JSON.parse(

        localStorage.getItem("favorites") || "[]"

    );



    // 已经收藏

    if(favorites.includes(name)){


        alert("已经收藏过该学校");

        return;

    }



    // 收藏数量限制20个

    if(favorites.length >= 20){


        alert("最多只能收藏20所学校");

        return;

    }



    // 按添加顺序保存

    favorites.push(name);



    localStorage.setItem(

        "favorites",

        JSON.stringify(favorites)

    );



    alert("收藏成功：" + name);



    showFavorites();


}







// =======================
// 显示收藏列表
// =======================


function showFavorites(){


    let favorites = JSON.parse(

        localStorage.getItem("favorites") || "[]"

    );



    let list = document.getElementById("favoriteList");



    if(list){


        list.innerHTML = "";



        favorites.forEach(function(item,index){



            let li = document.createElement("li");



            li.innerHTML =


            (index + 1) + ". " +


            '<a href="#" onclick="searchFavorite(\''

            + item +

            '\')">⭐ '


            + item +


            '</a>' +



            ' <button onclick="removeFavorite(\''

            + item +

            '\')">取消收藏</button>';



            list.appendChild(li);



        });



    }



}







// =======================
// 取消收藏
// =======================


function removeFavorite(name){


    let favorites = JSON.parse(

        localStorage.getItem("favorites") || "[]"

    );



    favorites = favorites.filter(function(item){


        return item !== name;


    });



    localStorage.setItem(

        "favorites",

        JSON.stringify(favorites)

    );



    showFavorites();



    alert("已取消收藏：" + name);



}







// =======================
// 点击收藏学校直接查询
// =======================


function searchFavorite(name){



    let input = document.getElementById("school");



    if(input){

        input.value = name;

    }




    let form = document.querySelector(".search-box");



    if(form){

        form.submit();

    }



}







// =======================
// 页面打开自动加载收藏
// =======================


window.onload = function(){


    showFavorites();


};
<script setup lang="ts">
function closeHelloScreen(e: Event) {
    let div = document.querySelector(".hideMenuBox");
    div.style.display = "block";
}

function handleParallax(e: MouseEvent) {
    let [x, y] = [e.clientX / 20, e.clientY / 20];

    let images = document.querySelectorAll(".parallax-image-outer");
    images.forEach((image, key) => {
        let transformCoef = key / 10 + 1;
        image.style.transform = `translateX(${x * transformCoef}px)  translateY(${y * transformCoef}px)`;
    });
}
</script>

<template>
    <div class="HelloScreen w-[100vw] h-[100vh] flex justify-center items-center gap-[50px] overflow-hidden"
         @mousemove="(e) => handleParallax(e)">
        <div class="HelloScreen__left">
            <h1 class="text-zinc-300 text-[3rem] font-bold">SkufTube</h1>
            <p class="text-zinc-300 mt-[10px] mb-[20px]">Первый и единственный сайт в своём роде</p>
            <button @click="(e) => closeHelloScreen(e)"
                    class="HelloScreen__btn py-[5px] px-[15px] rounded bg-[#37b084] text-[#ffffff] font-light">Начать
            </button>
        </div>
        <div class="HelloScreen__right flex relative w-[50%]">
            <div class="parallax-image-outer">
                <img src="/preview1.png" class="parallax-image" alt=""/>
            </div>
            <div class="parallax-image-outer z-10">
                <img src="/preview2.jpeg" class="parallax-image" alt="">
            </div>
            <div class="parallax-image-outer">
                <img src="/preview3.jpg" class="parallax-image" alt="">
            </div>
        </div>
        <div class="hideMenuBox"></div>
    </div>
</template>

<style scoped>

.hideMenuBox {
    box-shadow: rgba(11, 11, 11, 1) 10px 10px 50px;
    display: none;
    position: fixed;
    width: 100vw;
    height: 100vh;
    top: -100vh;
    right: 100vw;
    background: rgba(11, 11, 11, 1);
    border-radius: 0 0 50% 0;
    animation: hideMenu 2s forwards ease-out;
    z-index: 10;
}
.HelloScreen__btn:hover::before {
    transition: all .2s;
    position: absolute;
    content: "";
    background: rgba(55, 176, 132, 0.1);
    width: 100%;
    height: 100%;
    animation: buttonAnimationHover .3s ease-in-out;
    border-radius: 0.25rem;
    animation-fill-mode: forwards;
}

.HelloScreen__btn:focus {
    transition: all .2s;
    background: rgb(215, 255, 244);
    animation: buttonAnimationFocused .5s ease-in;
    animation-fill-mode: forwards;
}

.HelloScreen__btn {
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
}

.HelloScreen {
    background: rgb(11, 11, 11);
    background: linear-gradient(153deg, rgba(11, 11, 11, 1) 0%, rgba(13, 91, 79, 1) 49%, rgba(31, 220, 152, 1) 100%);
}

.HelloScreen__left {
    animation: showup 1.3s ease-in-out;
}

.HelloScreen__right {
    animation: appear 1.3s cubic-bezier(0, 0, 0, 1);
    position: relative;
    top: -75px;
}

.HelloScreen__right img {
    max-width: 400px;
    max-height: 500px;
    position: absolute;
    border-radius: 15px;
    box-shadow: #1e1e1e 2px 2px 10px;
}

.HelloScreen__right div:first-child img {
    transform: translateY(-50px);
    animation: wiggle 5s ease-in-out 1.3s infinite;
    z-index: 0;
}

.HelloScreen__right div:nth-child(2) img {
    animation: wiggle3d 5s ease-in-out .9s infinite;
    transform: perspective(500px) translateZ(100px) translateX(150px) translateY(0);
    z-index: 0;
}

.HelloScreen__right div:last-child img {
    animation: wiggle2 5s ease-in-out 1.5s infinite;
    transform: translateX(350px) translateY(-100px);
    z-index: 0;
}

/*@keyframes rotateGradient {
  from {
    background: rgb(11, 11, 11);
    background: linear-gradient(153deg, rgba(11, 11, 11, 1) 0%, rgba(13, 91, 79, 1) 49%, rgba(31, 220, 152, 1) 100%);
  }
  to {
    background: linear-gradient(720deg, rgba(11, 11, 11, 1) 0%, rgba(13, 91, 79, 1) 49%, rgba(31, 220, 152, 1) 100%);
  }
}*/

@keyframes showup {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

@keyframes appear {
    from {
        top: 300px;
    }
    to {
        top: -75px;
    }
}

@keyframes wiggle {
    0% {
        transform: translateY(-50px);
    }
    50% {
        transform: translateY(-40px);
    }
    100% {
        transform: translateY(-50px);
    }
}

@keyframes wiggle2 {
    0% {
        transform: translateX(350px) translateY(-100px);
    }
    50% {
        transform: translateX(350px) translateY(-90px);
    }
    100% {
        transform: translateX(350px) translateY(-100px);
    }
}

@keyframes wiggle3d {
    0% {
        transform: translateY(0) perspective(500px) translateZ(100px) translateX(150px);
    }
    50% {
        transform: translateY(10px) perspective(500px) translateZ(100px) translateX(150px);
    }
    100% {
        transform: translateY(0) perspective(500px) translateZ(100px) translateX(150px);
    }
}

@keyframes buttonAnimationHover {
    from {
        width: 100%;
        height: 100%;
    }
    to {
        height: 125%;
        width: 115%;
    }
}

@keyframes buttonAnimationFocused {
    from {
        background: rgb(215, 255, 244);
    }
    to {
        background: rgb(55, 176, 132);
    }
}

@keyframes hideMenu {
    from {
        width: 100vw;
        height: 100vh;
        right: 100vw;
        top: -100vh;
    }
    to {
        width: 200vw;
        height: 200vh;
        right: -100%;
        top: 0;
    }
}
</style>
<script setup lang="ts">
function closeHelloScreen(e: Event) {
  return;
}
function handleParallax(e: MouseEvent) {
  let [x, y] = [e.clientX / 20, e.clientY / 20];

  let images = document.querySelectorAll(".parallax-image-outer");
  images.forEach((image, key) => {
    let transformCoef = key / 10 + 1;

    image.style.transform = `translateX(${Math.floor(x) * transformCoef}px)  translateY(${Math.floor(y) * transformCoef}px)`;
  });
}
</script>

<template>
  <div class="HelloScreen w-[100vw] h-[100vh] flex justify-center items-center gap-[50px] overflow-hidden" @mousemove="(e) => handleParallax(e)">
    <div class="HelloScreen__left">
      <h1 class="text-zinc-300 text-[3rem] font-bold">SkufTube</h1>
      <p class="text-zinc-300 mt-[10px] mb-[20px]">Первый и единственный сайт в своём роде</p>
      <button @click="(e) => closeHelloScreen(e)" class="py-[5px] px-[15px] rounded bg-[#1fdc98] text-[#ffffff] font-light">Начать</button>
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
  </div>
</template>

<style scoped>
.HelloScreen {
  background: rgb(11,11,11);
  background: linear-gradient(153deg, rgba(11,11,11,1) 0%, rgba(13,91,79,1) 49%, rgba(31,220,152,1) 100%);
}
.HelloScreen__left {
  animation: showup 1.3s ease-in-out;
}
.HelloScreen__right {
  animation: appear 1.3s cubic-bezier(0,0,0,1);
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
  z-index: 1;
}
.HelloScreen__right div:last-child img {
  animation: wiggle2 5s ease-in-out 1.5s infinite;
  transform: translateX(350px) translateY(-100px);
  z-index: 0;
}

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
</style>
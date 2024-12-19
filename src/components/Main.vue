<template>

  <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <!-- <link href="https://fonts.googleapis.com/css?family=Google+Sans|Noto+Sans|Castoro" -->
    <!-- rel="stylesheet"> -->
  </head>
  <div class="main">
    <div class="section header">
      <div class="title"><img class="fire-icon" src="/icon2.png">MAT</div>
      <div class="subtitle">
        <!-- A Dataset for<br> -->
        <!-- <span class="uns">F</span>eedback <span class="uns">I</span>ntegration and -->
        <!-- <span class="uns">R</span>efinement <span class="uns">E</span>valuation -->
        <!-- <br>of Multimodal Models -->
        <span class="uns">M</span>ulti-modal <span class="uns">A</span>gent <span class="uns">T</span>uning: Building a
        VLM-Driven Agent for Efficient Tool Usage
        <!-- A Dataset for
        <span class="uns">F</span>eedback <span class="uns">I</span>ntegration and
        <br><span class="uns">R</span>efinement <span class="uns">E</span>valuation
        of Multimodal Models -->
      </div>

      <!-- <div> -->
      <!-- # write the conference name here,make it in the middle -->
      <!-- <div class="conference">NeurIPS 2024 Datasets and Benchmarks Track (Poster)</div>
      </div> -->

      <div class="author-list">

        <span class="author">
          <el-link href="https://zhigao2017.github.io/">Zhi Gao</el-link>
          <span class="ind">1,2 &#9733;</span>,
        </span>
        <span class="author">
          <el-link href="https://bofei5675.github.io/">Bofei Zhang</el-link>
          <span class="ind">2 &#9733;</span>,
        </span>
        <span class="author">
          <el-link href="https://pengxiang-li.github.io">Pengxiang Li</el-link>
          <span class="ind">2,3 &#9733;</span>,
        </span>
        <span class="author">
          <el-link href="https://jeasinema.github.io/">Xiaojian Ma</el-link>
          <span class="ind">2</span>,
        </span>
        <span class="author">
          <el-link href="https://yuefan1014.github.io/">Yue Fan</el-link>
          <span class="ind">2</span>,
        </span>
        <span class="author">
          <el-link href="https://i.yt.sb/">Tao Yuan</el-link>
          <span class="ind">2</span>,
        </span>
        <span class="author">
          <el-link href="https://wu-yuwei-bit.github.io/">Yuwei Wu</el-link>
          <span class="ind">&#9993;3,4</span>,
        </span>
        <br>

        <span class="author">
          <el-link href="https://scholar.google.com/citations?user=Sl6TV7gAAAAJ&hl=en">Yunde Jia</el-link>
          <span class="ind">4,3</span>,
        </span>
        <span class="author">
          <el-link href="https://www.zhusongchun.net/">Song-Chun Zhu</el-link>
          <span class="ind">2,1,5</span>,
        </span>
        <span class="author">
          <el-link href="https://liqing.io/">Qing Li</el-link>
          <span class="ind">&#9993;2</span>
        </span>
      </div>
      <div class="author-list">
        <span class="org">
          <span class="ind">1</span>
          Peking University
        </span>
        <span class="org">
          <span class="ind">2</span>
          Beijing Institute for Artificial General Intelligence
        </span>
        <br>
        <span class="org">
          <span class="ind">3</span>
          Beijing Institute of Technology
        </span>
        <span class="org">
          <span class="ind">4</span>
          Shenzhen MSU-BIT University
        </span>
        <span class="org">
          <span class="ind">5</span>
          Tsinghua University
        </span>
      </div>

      <!-- <div class="column has-text-centered"> -->
      <!-- <div class="publication-links"> -->

      <!-- <span class="link-block">
            <a href="https://arxiv.org/abs/2407.11522" class="external-link button is-normal is-rounded is-dark">
              <span class="icon">
                <svg xmlns="http://www.w3.org/2000/svg" width="1.0em" height="1.0em" viewBox="0 0 24 24">
                  <path fill="currentColor"
                    d="M3.842 0a1 1 0 0 0-.922.608c-.153.369-.044.627.294 1.111l6.919 8.36l-1.023 1.106a1.04 1.04 0 0 0 .003 1.423l1.23 1.313l-5.44 6.444c-.28.3-.453.823-.297 1.199a1.025 1.025 0 0 0 .959.635a.91.91 0 0 0 .689-.34l5.783-6.126l7.49 8.005a.85.85 0 0 0 .684.26a.96.96 0 0 0 .877-.615c.158-.377-.017-.75-.306-1.14L13.73 13.9l1.064-1.13a.963.963 0 0 0 .009-1.316L4.633.464S4.26.01 3.867 0zm0 .272h.017c.218.005.487.272.564.364l.005.006l.005.005l10.17 10.99a.69.69 0 0 1-.008.946l-1.066 1.133l-1.498-1.772l-8.6-10.39c-.328-.472-.352-.619-.26-.841a.73.73 0 0 1 .671-.44Zm14.341 1.57a.88.88 0 0 0-.655.242l-5.696 6.158l1.694 1.832l5.309-6.514c.325-.433.479-.66.325-1.029a1.12 1.12 0 0 0-.977-.689m-7.655 12.282l1.318 1.414l-5.786 6.13a.65.65 0 0 1-.496.26a.75.75 0 0 1-.706-.467c-.112-.269.036-.687.244-.909l.005-.005l.005-.006z" />
                </svg>
              </span>
              <span>arXiv</span>
            </a>
          </span> -->


      <!-- Video Link. -->
      <!-- <span class="link-block">
                <a href=""
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <i class="fab fa-youtube"></i>
                  </span>
                  <span>Video</span>
                </a>
              </span> -->
      <!-- Code Link. -->
      <!-- <span class="link-block">
            <a href="https://github.com/MM-FIRE/FIRE" class="external-link button is-normal is-rounded is-dark">
              <span class="icon">
                <i class="fab fa-github"></i>
              </span>
              <span>Code</span>
            </a>
          </span> -->

      <!-- Data Link. need changing -->
      <!-- <span class="link-block"> -->
      <!-- <a target="_blank" href="" -->
      <!-- <a target="_blank" href="https://huggingface.co/datasets/PengxiangLi/FIRE/"
              class="external-link button is-normal is-rounded is-dark">
              <span class="icon">
                <i class="fa fa-database"></i>
              </span>
              <span>Data</span>
            </a>
          </span> -->
      <!-- <span class="link-block"> -->
      <!-- <a target="_blank" href="" -->
      <!-- <a target="_blank" href="https://huggingface.co/li-qing/llava-next-llama3-8b-student-fire/tree/main"
              class="external-link button is-normal is-rounded is-dark">
              <span class="icon">
                <i class="fa fa-share-square"></i>
              </span>
              <span>Model</span>
            </a>
          </span> -->
      <!-- <span class="link-block"> -->
      <!-- <a target="_blank" href="" -->
      <!-- <a target="_blank" href="https://li-qing-fire.hf.space"
              class="external-link button is-normal is-rounded is-dark">
              <span class="icon">
                <i class="fa fa-images"></i>
              </span>
              <span>Demo</span>
            </a>
          </span>
          <span class="link-block"> -->
      <!-- <a target="_blank" href="" -->
      <!-- <a target="_blank" href="https://x.com/Sealiqing/status/1819279627438973133"
              class="external-link button is-normal is-rounded is-dark">
              <span class="icon">
                <svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="1.0em" height="1.0em"
                  viewBox="0,0,256,256">
                  <g fill="#e9e9e9" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt"
                    stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0"
                    font-family="none" font-weight="none" font-size="none" text-anchor="none"
                    style="mix-blend-mode: normal">
                    <g transform="scale(5.12,5.12)">
                      <path
                        d="M6.91992,6l14.2168,20.72656l-14.9082,17.27344h3.17773l13.13867,-15.22266l10.44141,15.22266h10.01367l-14.87695,-21.6875l14.08008,-16.3125h-3.17578l-12.31055,14.26172l-9.7832,-14.26172z">
                      </path>
                    </g>
                  </g>
                </svg>
              </span>
              <span>Twitter</span> -->
      <!-- </a> -->
      <!-- </span> -->
      <!-- <span class="link-block">
                <a href="file/clova_cvpr24_poster.pdf"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <i class="fas fa-file-pdf"></i>
                  </span>
                  <span>Poster (CVPR'24)</span>
                </a>
              </span> -->

      <!-- <span class="link-block">
                <a href="file/clova_slides.pdf"
                   class="external-link button is-normal is-rounded is-dark">
                  <span class="icon">
                      <i class="fas fa-file-pdf"></i>
                  </span>
                  <span>Slides</span>
                </a>
              </span> -->

      <!-- </div> -->
      <!-- </div> -->


    </div>


    <div class="tldr">
      <p><b>TL;DR</b> This paper proposes T3-Agent, a multi-modal agent tuned with the MM-Traj dataset for better
        tool-usage reasoning, boosting VLM performance by 20% on benchmarks.</p>
    </div>

    <div class="section">
      <el-card class="teaser">
        <el-image src="./teaser.png"></el-image>
      </el-card>
    </div>


    <div class="section">
      <div class="section-title">Introduction</div>
      <p class="intro">
        The advancement of large language models (LLMs) prompts the development of multi-modal agents, which are used as
        a controller to call external tools, providing a feasible way to solve practical tasks.
        In this paper, we propose a multi-modal agent tuning method that automatically generates multi-modal tool-usage
        data and tunes a vision-language model (VLM) as the controller for powerful tool-usage reasoning.
        To preserve the data quality, we prompt the GPT-4o mini model to generate queries, files, and trajectories,
        followed by query-file and trajectory verifiers.
        Based on the data synthesis pipeline, we collect the MM-Traj dataset that contains 20K tasks with trajectories
        of tool usage.
        Then, we develop the T3-Agent via  <span class="uns">T</span>rajectory  <span class="uns">T</span>uning on VLMs for  <span class="uns">T</span>ool usage
        using MM-Traj.
        Evaluations on the GTA and GAIA benchmarks show that the T3-Agent consistently achieves improvements on two
        popular VLMs: MiniCPM-V-8.5B and Qwen2-VL-7B, which outperforms untrained VLMs by 20%, showing the
        effectiveness of the proposed data synthesis pipeline, leading to high-quality data for tool-usage capabilities.
      </p>
    </div>
    <!-- 
      <div class="columns is-centered has-text-centered">
        <div class="column is-four-fifths">
          <div class="publication-video">

            <iframe width= 1120 height=630]  src="https://www.youtube.com/embed/PYPuZn8RjCE?si=3RO4hphplmbG_LJg"
            title="YouTube video player" frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen></iframe>
          </div>
        </div>
      </div> -->


    <!-- <div class="section">
      <div class="section-title">FIRE Dataset</div>
      <p>Notable statistics of <img class="fire-icon" src="/icon2.png"><b>FIRE</b></p>


         
      <el-card class="teaser">
        <el-image src="./stats/piechart.webp"></el-image>
      </el-card>
        <br>
            <el-card class="teaser">
        <el-image src="./stats/s1-6.png"></el-image>
      </el-card> -->
    <!-- <el-carousel :interval="8000" height="450px">
        <el-carousel-item>
          <el-image class="stats-img" src="./stats/piechart.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img" src="./stats/h1.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img" src="./stats/h2.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img" src="./stats/d1.webp"></el-image>
        </el-carousel-item>
      </el-carousel> -->
    <!-- </div> -->
    <!-- <div class="section">
      <div class="section-title">Dataset construction</div>
      <p class="intro">We build  <img class="fire-icon" src="/icon2.png"> <b>FIRE-1.1M</b> (FIRE-100K + FIRE-1M) for training: We first prompt GPT-4V to generate 100K high-quality feedback-refinement conversations from 27 source datasets. To scale up the training set, we train models on FIRE-100K and further simulate 1M dialogues as additional training data.</p>
         
      <el-card class="teaser">
        <el-image src="./stats/pipeline.webp"></el-image>
      </el-card>
      
    </div>

    <div class="section">
      <div class="section-title">Evaluation</div>
      <el-image class="stats-img" src="./eval1.webp"></el-image>
      <p class="intro">
        We design two evaluation settings: fixed dialogues and free dialogues to evaluate the performance of the student and teacher models.
        <br>
        <b>Fiexed dialogues.</b> In fixed dialogues, we evaluate whether the student and teacher models can generate appropriate responses and feedback given the conversation history, and their performance is evaluated by being compared with GPT-4V generated feedback and response, using the BLEU and CIDEr metrics to measure the textual alignment, mean absolute error (MAE) to evaluate the score given by the teacher model.
        <br>
        <b>Free dialogues.</b> We use a student model and a teacher model to perform free dialogues, and evaluate how fast and how much the student model can improve its answers based on the feedback from the teacher model. We introduce four metrics: average turn (AT), average dialogue refinement (ADR), average turn refinement (ATR), and refinement ratio (RR) for free dialogues. The AT metric evaluates how fast a VLM could achieve a satisfactory result based on feedback.  The ADR metric evaluates how much knowledge VLMs could learn from feedback in a dialogue. ATR evaluates how much knowledge VLMs could learn from feedback in one turn. RR measures the proportion of data that have a wrong initial response and a correct final response (i.e., how much data are corrected based on feedback). (Please refer to the paper for more details about the four metrics).
      
      
      </p> -->

    <!-- <el-card class="stats-img-1">
        <el-image src="./stats/Slide1.png"></el-image>
      </el-card>
        <br>
            <el-card class="stats-img-1">
        <el-image src="./stats/Slide2.png"></el-image>
      </el-card> -->


    <!-- <el-carousel :interval="8000" height="350px">
        <el-carousel-item>
          
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img-1" src="./results/fixed.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img-1" src="./results/fixed-teacher.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img-1" src="./results/free.webp"></el-image>
        </el-carousel-item>

        <el-carousel-item>
          <el-image class="stats-img" src="./results/acc_turn.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img" src="./results/atr_number.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img" src="./results/adr_number.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img" src="./results/rr_number.webp"></el-image>
        </el-carousel-item>
        <el-carousel-item>
          <el-image class="stats-img" src="./results/at_number.webp"></el-image>
        </el-carousel-item>

      </el-carousel> -->
    <!-- </div> -->
    <!-- <div class="section">
      <div class="section-title">Results</div>

    </div> -->

    <!-- <div class="section">
      <div class="section-title">Examples of FIRE-100K</div>
      <p class="intro">We randomly sampled some examples from FIRE-100K and show them here. </p>
      <el-carousel :interval="10000" type="card" height="1400px" indicator-position="none">
        <el-carousel-item v-for="d in dataset1" :key="d.id" :style="{ width: '1200px' }">
          <Dialog class="example-dialog" :data="d" />
        </el-carousel-item>
      </el-carousel>
    </div>

    <div class="section">
      <div class="section-title">Examples of FIRE-1M</div>
      <p class="intro">We randomly sampled some examples from FIRE-1M and show them here. </p>
      <el-carousel :interval="8000" type="card" height="1400px" indicator-position="none">
        <el-carousel-item v-for="d in dataset2" :key="d.id" :style="{ width: '1200px' }">
          <Dialog class="example-dialog" :data="d" />
        </el-carousel-item>
      </el-carousel>
    </div>
 
 
    <div class="section">
      <div class="section-title">Examples of FIRE-Bench</div>
      <p class="intro">We randomly sampled some examples from FIRE-Bench and show them here. </p>
      <el-carousel :interval="10000" type="card" height="1200px" indicator-position="none"> 
        <el-carousel-item v-for="d in dataset3" :key="d.id" :style="{ width: '1200px' }">
          <Dialog class="example-dialog" :data="d" />
        </el-carousel-item>
      </el-carousel>
    </div> -->
  </div>


  <!-- <section class="section" id="BibTeX" style="text-align: left;">
    <div class="container is-max-desktop content" style="max-width: 100%; margin: 0 auto;">
      <h3 class="title" style="font-size: small;">
        BibTeX
      </h3>
      <div class="bibtex-container">
        <pre><code class="language-bibtex">
          @article{li2024fire,
      title={FIRE: A Dataset for Feedback Integration and Refinement Evaluation of Multimodal Models},
      author={Li, Pengxiang and Gao, Zhi and Zhang, Bofei and Yuan, Tao and Wu, Yuwei and Harandi, Mehrtash and Jia, Yunde and Zhu, Song-Chun and Li, Qing},
      journal={Advances in Neural Information Processing Systems},
      year={2024}
      }
</code></pre>
      </div>
    </div>
  </section> -->


  <div class="footer">
    This website is inspired by <el-link href="https://mathvista.github.io/">MathVista</el-link> and <el-link
      href="https://nerfies.github.io/">Nerfies</el-link>.
  </div>
</template>

<script setup>
import Dialog from './Dialog.vue'

import { onMounted, ref } from 'vue'

const dataset1 = ref([])
const loadData1 = async () => {
  const resp1 = await fetch('./data/demo-100k.json')
  dataset1.value = await resp1.json()
}

const dataset2 = ref([])
const loadData2 = async () => {
  const resp2 = await fetch('./data/demo-1m.json')
  dataset2.value = await resp2.json()
}

const dataset3 = ref([])
const loadData3 = async () => {
  const resp3 = await fetch('./data/demo-bench.json')
  dataset3.value = await resp3.json()
}

onMounted(() => {
  loadData1(),
    loadData2(),
    loadData3()
})
</script>






<style scoped>
.main {
  text-align: center;
  color: #333;
}

.header {
  margin: 60px 0 0 0 !important;
}

.title {
  font-size: 5em;
}

.subtitle {
  font-size: 2.5em;
  color: #555;
}

.author-list {
  margin-top: 20px;
}

.author a {
  font-size: 1.2em;
  font-weight: normal;
  color: #337ecc;
}

.org {
  margin: 0 4px 0 4px;
}

.ind {
  font-size: 0.8em;
  vertical-align: super;
}

.section {
  margin: 50px 0;
}

.tldr {
  text-align: left;
  font-size: 1em;
  max-width: 1360px;
  line-height: 150%;
}

.section-title {
  margin: 20px;
  font-size: 2em;
  font-weight: bold;
}

.conference {
  text-align: center;
  margin: 20px;
  font-size: 1.5em;
  color: #665;
}

.uns {
  text-decoration: underline;
}

.fire-icon {
  width: 0.8em;
  height: 0.8em;
  margin-right: 0.2em;
}

.teaser {
  max-width: 840px;
  margin: 0 auto;
}

.stats-img {
  height: 300px;
}

.stats-img-1 {
  max-width: 95%;
  max-height: 95%;
  object-fit: contain;
}

.intro {
  text-align: justify;
  font-size: 1em;
  max-width: 1360px;
  line-height: 150%;
}

.link-block a {
  margin-top: 5px;
  margin-bottom: 5px;
}

.example-dialog {
  width: 800px;
}

.footer {
  color: #aaa;
  margin: 100px 0 60px 0;
}


/* The top button */
.external-link {
  display: inline-block;
  padding: 8px 16px;
  /* inner margin */
  margin: 4px;
  /* outer margin */
  border: 1px solid #9a9c9e;
  /* color of border */
  border-radius: 9px;
  background-color: #8a8b8b;
  color: white;
  text-decoration: none;
  font-size: 20px;
  transition: background-color 0.3s;
}

.external-link:hover {
  background-color: #8e8f90;
}

.external-link .icon {
  margin-right: 8px;
}

.external-link .fas {
  font-size: 18px;
}

.bibtex-container {
  background-color: #e1e4e9;
  /* Change background color to match the theme */
  padding: 1em;
  /* Add padding for better readability */
  border-radius: 5px;
  /* Add border radius for rounded corners */
  text-align: left;
  white-space: pre;
  /* Preserve formatting and prevent line breaks */
  overflow-x: auto;
  /* Add horizontal scroll bar */
}

pre {
  margin: 0;
}

code {
  font-family: 'Courier New', Courier, monospace;
  /* Change font to monospace */
  color: #0a0b0b;
  /* Change text color to match the theme */
}
</style>

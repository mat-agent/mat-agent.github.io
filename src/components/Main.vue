<template>

  <head>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.1/css/all.min.css">
    <!-- <meta charset="UTF-8"> -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
  </head>
  <div class="main">
    <div class="section header">
      <div class="title"><img class="mat-icon" src="/icon2.png">MAT</div>
      <div class="subtitle">
        <span class="uns">M</span>ulti-modal <span class="uns">A</span>gent <span class="uns">T</span>uning: Building a
        VLM-Driven Agent for Efficient Tool Usage

      </div>


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
          <span class="ind">1,2,5</span>,
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
          Beijing Institute for General Artificial Intelligence
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

      <span class="link-block">
        <a href="https://arxiv.org/pdf/2412.15606" class="external-link button is-normal is-rounded is-dark">
          <span class="icon">
            <svg xmlns="http://www.w3.org/2000/svg" width="1.0em" height="1.0em" viewBox="0 0 24 24">
              <path fill="currentColor"
                d="M3.842 0a1 1 0 0 0-.922.608c-.153.369-.044.627.294 1.111l6.919 8.36l-1.023 1.106a1.04 1.04 0 0 0 .003 1.423l1.23 1.313l-5.44 6.444c-.28.3-.453.823-.297 1.199a1.025 1.025 0 0 0 .959.635a.91.91 0 0 0 .689-.34l5.783-6.126l7.49 8.005a.85.85 0 0 0 .684.26a.96.96 0 0 0 .877-.615c.158-.377-.017-.75-.306-1.14L13.73 13.9l1.064-1.13a.963.963 0 0 0 .009-1.316L4.633.464S4.26.01 3.867 0zm0 .272h.017c.218.005.487.272.564.364l.005.006l.005.005l10.17 10.99a.69.69 0 0 1-.008.946l-1.066 1.133l-1.498-1.772l-8.6-10.39c-.328-.472-.352-.619-.26-.841a.73.73 0 0 1 .671-.44Zm14.341 1.57a.88.88 0 0 0-.655.242l-5.696 6.158l1.694 1.832l5.309-6.514c.325-.433.479-.66.325-1.029a1.12 1.12 0 0 0-.977-.689m-7.655 12.282l1.318 1.414l-5.786 6.13a.65.65 0 0 1-.496.26a.75.75 0 0 1-.706-.467c-.112-.269.036-.687.244-.909l.005-.005l.005-.006z" />
            </svg>
          </span>
          <span>arXiv</span>
        </a>
      </span>
      <span class="link-block">
        <a href="https://github.com/BIGAI-ML/TongAgent/tree/release" class="external-link button is-normal is-rounded is-dark">
          <span class="icon">
            <i class="fab fa-github"></i>
          </span>
          <span>Code</span>
        </a>
      </span>

      <!-- Data Link. need changing -->
      <!-- <span class="link-block">
 
        <a target="_blank" href="https://huggingface.co/datasets/PengxiangLi/FIRE/"
          class="external-link button is-normal is-rounded is-dark">
          <span class="icon">
            <i class="fa fa-database"></i>
          </span>
          <span>Data</span>
        </a>
      </span> -->
      <!-- <span class="link-block">
     
        <a target="_blank" href="https://huggingface.co/li-qing/llava-next-llama3-8b-student-fire/tree/main"
          class="external-link button is-normal is-rounded is-dark">
          <span class="icon">
            <i class="fa fa-share-square"></i>
          </span>
          <span>Model</span>
        </a>
      </span> -->
      <!-- <span class="link-block">
 
        <a target="_blank" href="https://li-qing-fire.hf.space"
          class="external-link button is-normal is-rounded is-dark">
          <span class="icon">
            <i class="fa fa-images"></i>
          </span>
          <span>Demo</span>
        </a>
      </span> -->
      <!-- <span class="link-block">
 
        <a target="_blank" href="https://x.com/Sealiqing/status/1819279627438973133"
          class="external-link button is-normal is-rounded is-dark">
          <span class="icon">
<svg xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="1.0em" height="1.0em" viewBox="0,0,256,256">
<g fill="#e9e9e9" fill-rule="nonzero" stroke="none" stroke-width="1" stroke-linecap="butt" stroke-linejoin="miter" stroke-miterlimit="10" stroke-dasharray="" stroke-dashoffset="0" font-family="none" font-weight="none" font-size="none" text-anchor="none" style="mix-blend-mode: normal"><g transform="scale(5.12,5.12)"><path d="M6.91992,6l14.2168,20.72656l-14.9082,17.27344h3.17773l13.13867,-15.22266l10.44141,15.22266h10.01367l-14.87695,-21.6875l14.08008,-16.3125h-3.17578l-12.31055,14.26172l-9.7832,-14.26172z"></path></g></g>
</svg>
          </span>
          <span>Twitter</span>
        </a>
      </span> -->
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
        Then, we develop the T3-Agent via <span class="uns">T</span>rajectory <span class="uns">T</span>uning on VLMs
        for <span class="uns">T</span>ool usage
        using MM-Traj.
        Evaluations on the GTA and GAIA benchmarks show that the T3-Agent consistently achieves improvements on two
        popular VLMs: MiniCPM-V-8.5B and Qwen2-VL-7B, which outperforms untrained VLMs by 20%, showing the
        effectiveness of the proposed data synthesis pipeline, leading to high-quality data for tool-usage capabilities.
      </p>
    </div>




    <video width="80%" height=auto controls="/poster.png">
      <source src="/mat-video.webm" type="video/webm">
    </video>


    <div class="section">
      <div class="section-title">Dataset Generation</div>
      <p class="intro"> We first prompt GPT-4o mini to generate <b>queries</b> and analyze what files are needed to
        solve the queries. Then, we produce files via two strategies. If needed files are images, we <b>search for them
          from existing image datasets</b>; otherwise, we prompt GPT-4o mini to <b>produce codes to generate the needed
          files</b>. Finally, we prompt a zero-shot agent to solve the generated tasks (i.e., queries and files) and
        collect trajectories, including the thoughts and codes in task solving. To preserve the data quality, the
        generated tasks and trajectories are passed through <b>two verifiers</b> to discard low-quality data. After
        that, we use these data to tune a VLM for efficient tool usage, through which one agent driven by the trained
        VLM could generate precise thoughts and codes for real-world tasks.</p>

      <el-card class="teaser">
        <el-image src="./stats/data_generation.jpg"></el-image>
      </el-card>

    </div>


    <div class="section">
      <div class="section-title">MM-Traj Dataset </div>
      <div class="intro">Data that passes through the two verifiers is considered high-quality and collected in an
        MM-Traj
        dataset. In summary, we collect <b>23.5K data points</b> from query generation and file generation. After
        passing through the two verifiers, <b>20K data points</b> are left with <b>15K files</b>. </div>
      <p>Notable statistics of <img class="mat-icon" src="/icon2.png"><b>MM-Traj</b></p>

      <br>
      <el-card class="teaser">
        <el-image src="./stats/stats-mm-traj.png"></el-image>
      </el-card>
    </div>




    <div class="section">
      <div class="section-title">
        <svg t="1735026864471" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"
          p-id="2411" width="35" height="35">
          <path
            d="M847.40096 805.88416c8.92544 8.92544 8.92544 23.00032-0.2752 32.50048a22.95552 22.95552 0 0 1-31.97696-0.54912L674.84288 697.78304a22.72512 22.72512 0 0 1 0.5248-32.22528c8.704-8.65024 23.296-8.65024 32.52608 0l139.5072 140.3264zM785.34784 15.4624a188.09216 188.09216 0 0 1 44.17664 4.62976 195.55456 195.55456 0 0 1 43.07712 13.00096 38.23744 38.23744 0 0 1 19.776 50.10176 40.4096 40.4096 0 0 1-7.87456 11.92576c-28.97664 28.97536-57.95328 57.6768-86.70464 86.67776l4.89984 17.3248 4.32512 17.6256 17.87648 4.84992 17.3504 4.60032c28.70144-28.97536 57.7024-57.42592 86.67904-86.67776 14.62656-14.90048 39.0016-14.90048 54.17856 0a38.84544 38.84544 0 0 1 9.19936 16.256 197.32992 197.32992 0 0 1 11.648 38.47552v0.5504h0.2752a229.60768 229.60768 0 0 1 4.32512 44.40192 223.29728 223.29728 0 0 1-223.20768 222.92096c-4.32512 0-8.65024-0.2752-13.00096-0.2752l-42.25152 41.728 232.41088 232.40576 1.89952 2.1504a156.99456 156.99456 0 0 1-1.89952 220.23168l-0.5504 0.5248a156.69632 156.69632 0 0 1-110.50496 45.52064c-40.0768 0-80.9792-15.1744-111.05536-46.05056L507.45984 725.68448 269.87392 963.79136c-49.55264 49.55136-109.43104 53.9264-158.464 32.77568a155.91936 155.91936 0 0 1-50.09408-33.8752h-0.27648a158.7584 158.7584 0 0 1-33.57696-49.82656c-21.15072-49.024-16.80128-109.15328 33.024-158.48064v-0.5248L325.4016 488.95616l-96.95488-96.97792-86.12864-25.728a37.59744 37.59744 0 0 1-24.37632-21.4016L35.28704 151.16416a38.048 38.048 0 0 1 6.77504-44.40064l34.67776-34.39872 34.15168-34.1504a37.67552 37.67552 0 0 1 41.70112-8.12544l196.11008 83.72736a37.43616 37.43616 0 0 1 21.67552 24.37632l25.45152 86.12736 96.97408 96.95616 69.632-69.05216c-0.2752-4.89984-0.5248-9.50016-0.5248-13.02528h0.2496a222.2208 222.2208 0 0 1 65.28-158.17984v-0.27904a224.13952 224.13952 0 0 1 157.9072-65.28zM675.9424 557.7536l-114.3296 114.3296 232.4352 232.40704a80.75904 80.75904 0 0 0 114.304 0.2496l0.5248-0.2496c15.72608-15.17568 23.0272-36.608 23.0272-57.1776a79.96416 79.96416 0 0 0-21.952-55.5264l-1.6-1.62432-232.4096-232.40832z m-296.88832-122.45248l59.8528-59.5776-103.72992-104.00256a38.33984 38.33984 0 0 1-10.30144-18.976l-22.49984-76.12672L146.368 110.816 130.39232 126.5408l-15.97568 16.256 66.32832 156.032 78.5536 23.00032a33.73056 33.73056 0 0 1 16.2752 10.02624l103.48032 103.45344z m400.896-343.43552a145.92 145.92 0 0 0-98.60224 43.32544 145.408 145.408 0 0 0-43.32672 104.00384h0.5248v10.57536l1.0752 8.92544c2.72512 11.92448-1.0752 24.94976-10.27584 34.432L114.41664 807.76192h-0.2752c-23.82592 24.65024-26.55104 52.55168-16.80128 75.5776a93.87136 93.87136 0 0 0 17.60128 25.472 87.296 87.296 0 0 0 26.00064 17.6c23.02592 10.02496 50.65216 7.296 75.05408-16.5248l263.83744-263.8336 1.0752-1.0752 167.936-168.2048 1.0752-1.37472 80.7296-80.17792h0.2496a36.23808 36.23808 0 0 1 32.256-11.10016 79.7696 79.7696 0 0 0 11.40096 1.09952c2.6752 0.2752 6.47552 0.5248 10.80064 0.5248a148.64128 148.64128 0 0 0 104.02944-42.52544v-0.5248a145.73568 145.73568 0 0 0 42.51904-98.60224c-16.52608 16.77568-33.05216 33.024-49.57824 50.10176-9.45024 10.54976-23.82592 14.90048-38.4512 11.62496l-38.4768-10.52544-38.97728-10.57536c-13.02528-3.52512-23.57632-12.99968-27.10144-27.10016l-10.30016-38.99776-10.57536-39.0016c-2.944-11.92448-0.2752-26.55104 10.02496-36.0256 17.07648-17.32608 34.15168-34.40128 51.47776-51.72736z"
            fill="#3B3F51" p-id="2412"></path>
        </svg> Tools in T3-Agent
      </div>
      <p class="intro">
        We deploy <b>real-executable tools</b> for the agent instead of only providing tool names. Our tools are across
        multiple categories: web search, visual perception, image generation/editing, file understanding, multi-modal
        understanding, and multiple Python packages.
      </p>
      <el-image class="stats-img" src="./stats/tools.png"></el-image>
    </div>



    <div class="section">
      <div class="section-title">Evaluation and Results </div>
      <div class="intro">We evaluate the <b>T3-Agent</b> on two benchmarks: <b>GTA</b> and <b>GAIA</b>. The results show
        that the T3-Agent
        consistently achieves improvements on two popular VLMs: <b>MiniCPM-V-8.5B</b> and <b>Qwen2-VL-7B</b>, which
        outperforms
        untrained VLMs by 20%, showing the effectiveness of the proposed data synthesis pipeline, leading to
        high-quality data for tool-usage capabilities.<br></div>

      <div class="intro"><b>Metric.</b> In the <b>GTA</b> benchmark, we measure three metrics for agents, including
        <i><b>AnsAcc</b></i>,
        <i><b>ToolAcc</b></i>, and <i><b>CodeExec</b></i>. <i><b>AnsAcc</b></i> measures the correctness of predicted
        answers. <i><b>ToolAcc</b></i> means the accuracy of tool selection and answer summary. <i><b>CodeExec</b></i>
        quantifies the percentage of generated codes that could be executed without errors. In the <b>GAIA</b>
        benchmark, we measure <i><b>AnsAcc</b></i> of its three levels.<br><br>
      </div>

      <div class="intro"><b>GTA Results.</b> Our agent outperforms both the closed-source Lego agent (e.g., GPT-4) and
        the open-source HF agent (e.g., InternVL2-8B) in solving complex tasks, demonstrating the effectiveness of our
        multimodal agent tuning method. For instance, tuning MiniCPM-V-8.5B improves answer accuracy, tool correctness,
        and code executability by 18%, 29%, and 24%, respectively. While our agent achieves higher ToolAcc than the HF
        agent, its weaker programming capability results in lower CodeExec and AnsAcc, highlighting the need to enhance
        VLMs for coding tasks.<br></div>
      <el-card class="stats-img-1">
        <el-image src="./stats/gta-results.png"></el-image>
      </el-card>
      <div class="intro"><b>GAIA Results.</b> T3-Agent outperforms agents using open-source models, such as Qwen2-VL-7B,
        exceeding its performance by 10%. These improvements across various VLMs validate the effectiveness of our
        dataset. However, T3-Agent performs worse than closed-source models (e.g., GPT-4) due to their larger model
        sizes and more extensive training data, which likely drive the performance gap.<br></div>
      <el-card class="stats-img-1">
        <el-image src="./stats/gaia-results.png"></el-image>
      </el-card>
    </div>


  </div>


  <section class="section" id="BibTeX" style="text-align: left;">
    <div class="container is-max-desktop content" style="max-width: 100%; margin: 0 auto;">
      <h3 class="title" style="font-size: small;">
        BibTeX
      </h3>
      <div class="bibtex-container">
        <pre><code class="language-bibtex">
    @article{gao2024multimodalagenttuningbuilding,
      title={Multi-modal Agent Tuning: Building a VLM-Driven Agent for Efficient Tool Usage}, 
      author={Zhi Gao and Bofei Zhang and Pengxiang Li and Xiaojian Ma and Tao Yuan and Yue Fan and Yuwei Wu and Yunde Jia and Song-Chun Zhu and Qing Li},
      year={2024},
      eprint={2412.15606},
      archivePrefix={arXiv},
      primaryClass={cs.AI},
      url={https://arxiv.org/abs/2412.15606}, 
    }
</code></pre>
      </div>
    </div>
  </section>


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

.mat-icon {
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
  max-width: 67%;
  max-height: 95%;
  object-fit: contain;
  margin: 0 auto;
  display: block;
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

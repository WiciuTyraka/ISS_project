<template>
  <div>


<div class="d-flex justify-content-around" id="title">
  <div class="p-2" ><h1 class="display-2"><b>ISS Project</b></h1></div>
  <div class="p-2">some descriptionsome descriptionsome descriptionsome descriptionsome descriptionsome <br/>descriptionsome descriptionsome descriptionsome descriptionsome descriptionsome description <br/>descriptionsome descriptionsome descriptionsome descriptionsome descriptionsome description <br/>descriptionsome descriptionsome descriptionsome descriptionsome descriptionsome description <br/> </div>
</div>

<b-form @submit="onSubmit" @reset="onReset" v-if="show">

<div id="modelParams">
<h1><b>Model Parameters</b></h1>
<div class="d-flex flex-column">
  <div class="p-2">
    <div class="d-flex justify-content-center">
    <div class="p-2" id='motorDescription'>some desriptionsome desriptiosome desriptiosome desriptio</div>
    <div class="p-2">
      <div class="d-flex flex-column">
      <div class="p-2">
        <div class="d-flex flex-row">
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="motor axis radius" label-for="input-1">
              <b-form-input  id="input-1" type="number" step="0.001" min="0.00" max="100.00" v-model.number="form.motorAxisRadius"  placeholder="Enter motor axis radius"  required></b-form-input>
            </b-form-group>
          </div>
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="motor axis length" label-for="input-2" >
              <b-form-input id="input-2" type="number" step="0.0001" min="0.00" max="10.00" v-model.number="form.motorAxisLength" placeholder="Enter motor axis length" required></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
      <div class="p-2">
        <div class="d-flex flex-row">
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="steel density" label-for="input-3" >
              <b-form-input id="input-3" type="number" step="1" min="0.00" max="10000.00" v-model.number="form.steelDensity" placeholder="Enter steel density" required></b-form-input>
            </b-form-group>
          </div>
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="ratedt torque" label-for="input-4" >
              <b-form-input id="input-4" type="number" step="0.001" min="0.00" max="10.00" v-model.number="form.ratedTorque" placeholder="Enter ratedt torque" required></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
      <div class="p-2">
        <div class="d-flex flex-row">
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="rated current" label-for="input-5" >
              <b-form-input id="input-5" type="number" step="0.01" min="0.00" max="10.00" v-model.number="form.ratedCurrent" placeholder="Enter rated current" required></b-form-input>
            </b-form-group>
          </div>
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="rated speed" label-for="input-6" >
              <b-form-input id="input-6" type="number" step="0.01" min="0.00" max="1000.00" v-model.number="form.ratedSpeed" placeholder="Enter rated speed" required></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
      <div class="p-2"><div class="d-flex flex-row">
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="inductance" label-for="input-7" >
              <b-form-input id="input-7" type="number" step="0.0001" min="0.00" max="10.00" v-model.number="form.inductance" placeholder="Enter inductance" required></b-form-input>
            </b-form-group>
          </div>
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="resistance" label-for="input-8" >
              <b-form-input id="input-8" type="number" step="0.01" min="0.00" max="100.00" v-model.number="form.resistance" placeholder="Enter resistance" required></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
      <div class="p-2">
        <b-form-group id="input-group-9" label="rated voltage" label-for="input-9" >
          <b-form-input id="input-9" type="number" step="0.1" min="0.00" max="100.00" v-model.number="form.ratedVoltage" placeholder="Enter rated voltage" required></b-form-input>
        </b-form-group>
      </div>
</div>
    </div>
  </div>
</div>
</div>

  
  <div class="p-2">
    <div class="d-flex justify-content-center">
      <div class="p-2" id='pidDescription'>some desriptionsome desriptiosome desriptiosome desriptio <br/> some desriptionsome desriptiosome desriptiosome desriptio </div>
      <div class="p-2">
        <div class="d-flex flex-column">
          <div class="p-2">
            <b-form-group id="input-group-10" label="Kp value" label-for="input-10" >
              <b-form-input id="input-10" type="number" step="0.001" min="0.00" max="100.00" v-model.number="form.kp" placeholder="Enter Kp value" required></b-form-input>
            </b-form-group>
          </div>
          <div class="p-2">
            <b-form-group id="input-group-11" label="Ti value" label-for="input-11" >
              <b-form-input id="input-11" type="number" step="0.001" min="0.00" max="1000.00" v-model.number="form.Ti" placeholder="Enter Ti value" required></b-form-input>
            </b-form-group>
          </div>
          <div class="p-2">
            <b-form-group id="input-group-12" label="Td value" label-for="input-12" >
              <b-form-input id="input-12" type="number" step="0.0001" min="0.00" max="10.00" v-model.number="form.Td" placeholder="Enter Td value" required></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="p-2">
    <div class="d-flex justify-content-center">
      <div class="p-2" id='wheelDescription'>some desriptionsome desriptiosome desriptiosome desriptio</div>
      <div class="p-2">
        <div class="d-flex flex-row">
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="wheel radius" label-for="input-13" >
              <b-form-input id="input-13" type="number" step="0.001" min="0.00" max="10.00" v-model.number="form.wheelRadius" placeholder="Enter wheel radius" required></b-form-input>
            </b-form-group>
          </div>
          <div class="p-2">
            <b-form-group id="modelParamsSmall" label="track of wheel" label-for="input-14" >
              <b-form-input id="input-14" type="number" step="0.1" min="0.00" max="100.00" v-model.number="form.trackOfWheel" placeholder="Enter track of wheel" required></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
    </div>  
  </div>
</div>

<div class="d-flex justify-content-center">
  <div class="p-2">
    <div id="simulationParams" class="d-flex flex-column">
      <div class="p-2"><h1><b>Simulation parameters</b></h1></div>
      <div class="p-2">
        <b-form-group id="input-group-14" label="tracjectory" label-for="input-14">
          <b-form-select id="input-14" v-model="form.tracjectory" :options="tracjectory" required></b-form-select>
        </b-form-group>
      </div>
      <div class="p-2">
        <div class="d-flex flex-row">
          <div class="p-2">
            <b-form-group id="simulationParamsSmall" label="smapling time" label-for="input-15" >
              <b-form-input id="input-15" type="number" step="0.0001" min="0.00" max="1000.00" v-model.number="form.samplingTime" placeholder="Enter smapling time" required></b-form-input>
            </b-form-group>
          </div>
            <div class="p-2"><b-form-group id="simulationParamsSmall" label="time of simulation" label-for="input-16" >
              <b-form-input id="input-16" type="number" step="0.01" min="0.00" max="1000.00" v-model.number="form.timeOfSimulation" placeholder="Enter time of simulation" required></b-form-input>
            </b-form-group></div>
          </div>
      </div>
      <div class="p-2">
        <div class="d-flex flex-row">
          <div class="p-2">
            <b-form-group id="simulationParamsSmall" label="trajectory circle radius" label-for="input-17" >
              <b-form-input id="input-17" type="number" step="0.1" min="0.00" max="100.00" v-model.number="form.trajectoryCircleRadius" placeholder="Enter trajectory circle radius" required></b-form-input>
            </b-form-group>
          </div>
            <div class="p-2"><b-form-group id="simulationParamsSmall" label="trajectory circle period" label-for="input-18" >
              <b-form-input id="input-18" type="number" step="0.1" min="0.00" max="100.00" v-model.number="form.trajectoryCirclePeriod" placeholder="Enter trajectory circle period" required></b-form-input>
            </b-form-group></div>
        </div>
       </div>
      <div class="p-2">
        <div class="d-flex flex-row">
          <div class="p-2">
            <b-form-group id="simulationParamsSmall" label="trajectory A Coefficient" label-for="input-19" >
              <b-form-input id="input-19" type="number" step="0.1" min="0.00" max="100.00" v-model.number="form.trajectoryACoefficient" placeholder="Enter trajectory A Coefficient" required></b-form-input>
            </b-form-group>
          </div>
          <div class="p-2">
            <b-form-group id="simulationParamsSmall" label="trajectory B Coefficient" label-for="input-20" >
              <b-form-input id="input-20" type="number" step="0.1" min="0.00" max="100.00" v-model.number="form.trajectoryBCoefficient" placeholder="Enter trajectory B Coefficient" required></b-form-input>
            </b-form-group>
          </div>
        </div>
      </div>
        <div class="p-2">
        <div class="d-flex justify-content-center">
          <div class="p-2">
            <b-button type="button" @click="handleClick" class="btn btn-info">Set default</b-button>
          </div>
          <div class="p-2">
            <b-button type="submit" variant="primary">Submit</b-button>
          </div>
          <div class="p-2">
            <b-button type="reset" variant="danger">Reset</b-button>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="p-2">
    <div class="d-flex flex-column" id="plotTrajectory">
      <div class="p-2" id="plotTitle"><h2><b>Trajectory</b></h2></div>
      <div class="p-2">
         <div>
           <pulse-loader id="load" :loading="loading" :color="color" :size="size"></pulse-loader>
           <!-- <Plot msg="ploter" id="plot3"/> -->
          <img v-bind:src="'data:image/jpg;base64, ' + image.imag3" />
         </div>
      </div>
    </div>
  </div>
</div>


<div class="d-flex justify-content-center" id="plotwheel">
  <div class="p-2">
    <div class="d-flex flex-column">
      <div class="p-2" id="plotTitle"><h2><b>Right wheel</b></h2></div>
      <div class="p-2">
        <pulse-loader id="load" :loading="loading" :color="color" :size="size"></pulse-loader>
        <!-- <Plot msg="ploter" id="plot1"/> -->
        <img v-bind:src="'data:image/jpg;base64, ' + image.imag1" />
      </div>
    </div>
  </div>
  <div class="p-2">
    <div class="d-flex flex-column">
      <div class="p-2" id="plotTitle"><h2><b>Left wheel</b></h2></div>
      <div class="p-2">
        <pulse-loader id="load" :loading="loading" :color="color" :size="size" :is-full-page=true></pulse-loader>
        <!-- <Plot msg="ploter" id="plot2"/> -->
        <img v-bind:src="'data:image/jpg;base64, ' + image.imag2" />
      </div>
    </div>
  </div>
</div>



    </b-form>
    <div id="autographs"><h6><em>ISS project by </em>   Adam Sawościanik &amp; Adam Zdunek &amp; Bartosz Musiał &amp; Wiktor Tasarek</h6></div>

  </div>
</template>

<script>

import PulseLoader from "vue-spinner/src/PulseLoader.vue";
// import Plot from './Plots.vue'
// import '@/plugin/apexcharts'


  const axios = require('axios');
  const {emptyPlot} = require('../assets/plot');


  export default {
    data() {
      return {
        form: {
          motorAxisRadius: '',
          motorAxisLength: '',
          steelDensity: '',
          ratedTorque: '',
          ratedCurrent: '',
          ratedSpeed: '',
          inductance: '',
          resistance: '',
          ratedVoltage: '',
          kp: '',
          Ti: '',
          Td: '',
          wheelRadius: '',
          trackOfWheel: '',
          tracjectory: null,
          samplingTime: '',
          timeOfSimulation: '',
          trajectoryCircleRadius: '',
          trajectoryCirclePeriod: '',
          trajectoryACoefficient: '',
          trajectoryBCoefficient: '',
        },
        color: '#00587c',
        loading: false,
        
        tracjectory: [{ text: 'Select trajectory', value: null }, {text: 'Ring', value: 1 }, {text: 'Lissajous curve', value: 2}],
        show: true,
        image: {
          imag1: emptyPlot,
          imag2: emptyPlot,
          imag3: emptyPlot,
        },
      }     
    },
    components: {
        PulseLoader,
        //Plot,
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        //alert(JSON.stringify(this.form))
        this.loading = true
        var simulationDataJson = JSON.stringify(this.form)

        console.log(simulationDataJson)
      
        axios.post('http://localhost:8090/postjson', this.form )
          
         .then( (response) => {
           console.log(response);
           this.loading = false
           this.image.imag1 = response.data.plot1;
           this.image.imag2 = response.data.plot2;
           this.image.imag3 = response.data.plot3;
         })
         .catch((error) => {
           console.log(error);
         });

      },
      handleClick: function(){
        this.form.motorAxisRadius= 0.003,
        this.form.motorAxisLength= 0.0409,
        this.form.steelDensity= 7500,
        this.form.ratedTorque= 0.002,
        this.form.ratedCurrent= 0.3,
        this.form.ratedSpeed= 680.68,
        this.form.inductance= 0.002,
        this.form.resistance= 3.2,
        this.form.ratedVoltage= 12.0,
        this.form.kp= 7.0,
        this.form.Ti= 155.0,
        this.form.Td= 0.001,
        this.form.wheelRadius= 0.025,
        this.form.trackOfWheel= 12.00,
        this.form.tracjectory= 1,
        this.form.samplingTime= 0.0001,
        this.form.timeOfSimulation= 10,
        this.form.trajectoryCircleRadius= 0.20,
        this.form.trajectoryCirclePeriod= 10,
        this.form.trajectoryACoefficient= 1,
        this.form.trajectoryBCoefficient= 2
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.motorAxisRadius = ''
        this.form.motorAxisLength = ''
        this.form.steelDensity = ''
        this.form.ratedTorque = ''
        this.form.ratedCurrent = ''
        this.form.ratedSpeed = ''
        this.form.inductance = ''
        this.form.resistance = ''
        this.form.ratedVoltage = ''
        this.form.kp = '',
        this.form.Ti = '',
        this.form.Td = '',
        this.form.wheelRadius = '',
        this.form.trackOfWheel = '',
        this.form.tracjectory = null
        this.form.samplingTime = '',
        this.form.timeOfSimulation = '',
        this.form.trajectoryCircleRadius = '',
        this.form.trajectoryCirclePeriod = '',
        this.form.trajectoryACoefficient = '',
        this.form.trajectoryBCoefficient = '',

        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>

<style>
#input-10 {
  width: 470px

}

#modelParamsSmall {
  width: 200px
}

#simulationParamsSmall {
  width: 200px
}

#motorDescription {
  margin-top: 300px;
  margin-left: -100px;
  margin-right: 100px;
}

#pidDescription {
  margin-top: 130px;
  margin-left: -100px;
  margin-right: 100px;
}

#wheelDescription {
  margin-top: 50px;
  margin-left: -100px;
  margin-right: 100px;
}

#modelParams {
  margin: 70px;
  margin-top: 60px;
  padding-top: 60px;
  padding-bottom: 60px;
  border-radius: 100px;
  background-color: #00587c;
  color: #ffffff;
}

#simulationParams {
  margin: 50px;
  border-radius: 50px;
  padding: 40px;
  margin-top: 20px;
  background-color: #00587c;
  color: #ffffff;
}

#plotTitle {
  margin: -70px;
}

#plotTrajectory {
  padding-top: 170px;
}

#plotwheel {
  padding-top: 70px;
  padding-bottom: 40px;
}

#autographs {
  background-color: #404242;
  color: #ffffff;
  padding: 20px;
}

#title {
  padding: 40px;
}

#load {
  margin-top: 50px ;
}

</style>
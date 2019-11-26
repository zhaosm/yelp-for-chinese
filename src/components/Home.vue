<template>
  <div>
    <v-row no-gutters>
  <v-app-bar
      color="amber"
    >
    <span class="title ml-3 mr-5">Yelp For Chinese</span>
    <v-text-field
      solo-inverted
      flat
      hide-details
      label="Search"
    />
    <v-btn text icon>
      <v-icon>mdi-magnify</v-icon>
    </v-btn>
  </v-app-bar>
    </v-row>
  <!--<v-row no-gutters>-->
    <!--<v-col class="text-center" cols="3">-->
      <!--<div class="my-1">-->
        <!--<v-btn block>Burgers</v-btn>-->
      <!--</div>-->
    <!--</v-col>-->
    <!--<v-col class="text-center" cols="3">-->
      <!--<div class="my-1">-->
        <!--<v-btn block>Italian</v-btn>-->
      <!--</div>-->
    <!--</v-col>-->
    <!--<v-col class="text-center" cols="3">-->
      <!--<div class="my-1">-->
        <!--<v-btn block>Chinese</v-btn>-->
      <!--</div>-->
    <!--</v-col>-->
    <!--<v-col class="text-center" cols="3">-->
      <!--<div class="my-1">-->
        <!--<v-btn block>Mexican</v-btn>-->
      <!--</div>-->
    <!--</v-col>-->
  <!--</v-row>-->


    <v-row no-gutters>
      <v-col
        v-for="(item, i) in items"
        :key="i"
        cols="12"
        class="my-1"
      >
        <v-card>
          <div class="d-flex flex-no-wrap justify-space-between">
            <!--avatar-->
            <v-avatar
              class="mx-3 my-auto"
              style="border-radius: 3%;"
              size="250"
              tile
            >
              <v-img :src="item.img"></v-img>
            </v-avatar>

            <!--basic information-->
            <v-col cols="3">
              <v-card-title
                class="headline"
                v-text="item.name"
              ></v-card-title>
              <v-card-text>
                <v-row
                  align="center"
                  class="mx-0"
                >
                  <v-rating
                    :value="item.rating"
                    color="amber"
                    dense
                    half-increments
                    readonly
                    size="14"
                  ></v-rating>

                  <div class="grey--text ml-4">{{ item.rating }} ({{item.numReviews}} reviews)</div>
                </v-row>

                <div class="subtitle-1 my-3">
                  <span v-for="n in item.cost" :key="n" class="black--text">$</span> <span class="grey--text">• {{ item.type }}</span>
                </div>
                <div class="subtitle-1 black--text my-1">
                  {{ item.phone }}
                </div>
                <div class="subtitle-1 black--text my-1">
                  {{ item.address }}
                </div>
                <div class="subtitle-1 black--text my-1">
                  {{ item.neighborhood }}
                </div>
              </v-card-text>
            </v-col>

            <!--popular review-->
            <div>
              <v-card-text>
                {{ item.popularReview }}
              </v-card-text>
            </div>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </div>

</template>

<script>
  export default {
    data: () => ({
      items: [
        {
          img: 'https://s3-media0.fl.yelpcdn.com/bphoto/hd7Ith2Gm3QnrQqOzI_JvA/ls.jpg',
          rank: 1,
          rating: 4.5,
          numReviews: 3019,
          cost: 2,
          name: 'Poor Calvin\'s',
          type: 'Asian Fusion, Southern, Comfort Food',
          phone: '(404) 254-4051',
          address: '510 Piedmont Ave NE',
          neighborhood: 'Downtown',
          popularReview: '“Amazing place! Took an off from work just to experience this place! It was so worth it! Amazing food. Tried \'The Beast\' sandwich and the \'shawrma platter\'.…”'
        },
        {
          img: 'https://s3-media0.fl.yelpcdn.com/bphoto/_x61pM4WZiji4d2jq1GnYw/ls.jpg',
          rank: 2,
          rating: 5.0,
          numReviews: 1433,
          cost: 2,
          name: 'Aviva by Kameel',
          type: 'Mediterranean, Juice Bars & Smoothies, Middle Eastern',
          phone: '(404) 698-3600',
          address: '225 Peachtree St NE',
          neighborhood: 'Downtown',
          popularReview: '“Hubby and I were in town for the weekend from CA and wanted to try some yummy fried chicken so took to Yelp to search. Came across Gus\'s and was super happy…”'
        },
      ],
    }),
  }
</script>
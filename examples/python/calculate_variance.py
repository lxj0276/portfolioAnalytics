# encoding: utf-8

# (c) 2014-2019 Open Risk (https://www.openriskmanagement.com)
#
# TransitionMatrix is licensed under the Apache 2.0 license a copy of which is included
# in the source distribution of TransitionMatrix. This is notwithstanding any licenses of
# third-party software included in this distribution. You may not use this file except in
# compliance with the License.
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.

import json
from portfolioAnalytics.variance import Portfolio, variance
from portfolioAnalytics import dataset_path

json_data=open(dataset_path + '/portfolio_data1.json').read()
data = json.loads(json_data)
print(data)

P = Portfolio()
P.loadjson(data)
print(variance(P))

